from django.urls import path
from . import views

# API URL patterns
urlpatterns = [
    path('stores/', views.StoreList.as_view(), name='store-list'),
    path('stores/<int:store_id>/', views.StoreDetailUpdateDelete.as_view(), name='store_detail'),
    path('stores/deleteAll/', views.StoreDeleteAll.as_view(), name='store_delete_all'),
    path('products/', views.ProductList.as_view(), name='product-list'),
    path('products/<int:id>/', views.ProductDetailUpdateDelete.as_view(), name='product_detail'),
    path('products/deleteAll/', views.ProductDeleteAll.as_view(), name='product_delete_all'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('customers/', views.CustomerList.as_view(), name='customer-list'),
    path('customers/<int:pk>/', views.CustomerDetail.as_view(), name='customer-detail'),
    path('orders/', views.OrderList.as_view(), name='order-list'),
    path('orders/<int:pk>/', views.OrderDetail.as_view(), name='order-detail'),
    path('reviews/', views.ReviewList.as_view(), name='review-list'), # Supports customer_id now
    path('reviews/<str:pk>/', views.ReviewDetail.as_view(), name='review-detail'),
    path('connect-db/', views.check_db_connection, name='check-db'),
]
