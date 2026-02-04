from rest_framework import response
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse

from .stores import StoreList, StoreDetailUpdateDelete, StoreDeleteAll
from .products import ProductList, ProductDetailUpdateDelete, ProductDeleteAll
from .users import UserList, UserDetail
from .orders import OrderList, OrderDetail
from .reviews import ReviewList, ReviewDetail
from .customers import CustomerList, CustomerDetail
from .db_check import check_db_connection

@api_view(['GET'])
def api_root(request, format=None):
    return response.Response({
        'stores': reverse('store-list', request=request, format=format),
        'products': reverse('product-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
        'customers': reverse('customer-list', request=request, format=format),
        'orders': reverse('order-list', request=request, format=format),
        'reviews': reverse('review-list', request=request, format=format),
        'check-db': reverse('check-db', request=request, format=format),
    })
