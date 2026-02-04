from rest_framework import response, status
from rest_framework.views import APIView
from ..mongo_utils import get_db_handle
from datetime import datetime
from bson import ObjectId
from ..models import Customer

class ReviewList(APIView):
    # API view to manage Reviews using MongoDB
    
    def get(self, request):
        # List all reviews or filter by product_id
        db = get_db_handle()
        collection = db['reviews']
        
        product_id = request.query_params.get('product_id')
        filter_query = {}
        if product_id:
            filter_query['product_id'] = int(product_id)
        
        # Convert ObjectId to string for JSON serialization
        reviews = list(collection.find(filter_query))
        
        # Enrich with Customer data from SQL
        customer_ids = [review.get('customer_id') for review in reviews if review.get('customer_id')]
        customers = Customer.objects.filter(id__in=customer_ids).values('id', 'name')
        customer_map = {customer['id']: customer['name'] for customer in customers}

        for review in reviews:
            review['_id'] = str(review['_id'])
            customer_id = review.get('customer_id')
            review['customer_name'] = customer_map.get(customer_id, "Unknown Customer")
            
        return response.Response(reviews)

    def post(self, request):
        # Create a new review
        # Sample Data:
        # {
        #     "product_id": 1,
        #     "customer_id": 1,
        #     "rating": 5,
        #     "comment": "Great product!"
        # }
        db = get_db_handle()
        collection = db['reviews']
        
        data = request.data
        review = {
            'product_id': data.get('product_id'),
            'customer_id': data.get('customer_id'),
            'rating': data.get('rating'),
            'comment': data.get('comment'),
            'created_at': datetime.now().isoformat()
        }
        
        result = collection.insert_one(review)
        review['_id'] = str(result.inserted_id)
        
        return response.Response(review, status=status.HTTP_201_CREATED)

class ReviewDetail(APIView):
    # API view to retrieve, update or delete a specific review from MongoDB
    
    def get_object(self, pk):
        db = get_db_handle()
        collection = db['reviews']
        try:
            return collection.find_one({'_id': ObjectId(pk)})
        except:
            return None

    def get(self, request, pk):
        review = self.get_object(pk)
        if review:
            review['_id'] = str(review['_id'])
            return response.Response(review)
        return response.Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        db = get_db_handle()
        collection = db['reviews']
        
        existing_review = self.get_object(pk)
        if not existing_review:
            return response.Response(status=status.HTTP_404_NOT_FOUND)

        data = request.data
        update_data = {k: v for k, v in data.items() if k in ['rating', 'comment', 'product_id', 'customer_id']}
        update_data['updated_at'] = datetime.now().isoformat()
        
        collection.update_one({'_id': ObjectId(pk)}, {'$set': update_data})
        
        updated_review = collection.find_one({'_id': ObjectId(pk)})
        updated_review['_id'] = str(updated_review['_id'])
        
        return response.Response(updated_review)

    def delete(self, request, pk):
        db = get_db_handle()
        collection = db['reviews']
        
        result = collection.delete_one({'_id': ObjectId(pk)})
        if result.deleted_count > 0:
            return response.Response(status=status.HTTP_204_NO_CONTENT)
        return response.Response(status=status.HTTP_404_NOT_FOUND)

