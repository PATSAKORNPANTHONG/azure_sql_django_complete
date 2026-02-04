import certifi
from pymongo import MongoClient
from django.conf import settings

_client = None

def get_db_handle():
    global _client
    try:
        if _client is None:
            _client = MongoClient(settings.MONGO_URI, tlsCAFile=certifi.where())
        
        db = _client[settings.MONGO_DB_NAME]
        return db
    except Exception as e:
        print(f"Error connecting to MongoDB: {e}")
        raise e
