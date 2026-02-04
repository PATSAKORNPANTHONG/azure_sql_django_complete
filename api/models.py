from datetime import timezone
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Store(models.Model):
    # Model representing a physical store location
    store_id = models.IntegerField(unique=True)
    store_location = models.CharField(max_length=100)

    # String representation of the store
    def __str__(self):
        return f"{self.store_id} - {self.store_location}"

class Customer(models.Model):
    # Model representing a customer
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Product(models.Model):
    # Model representing a product available in a store
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    # String representation of the product
    def __str__(self):
        return self.name

class Order(models.Model):
    # Model representing a customer order
    STATUS_CHOICES = [
        ('PENDING', 'Pending'),
        ('COMPLETED', 'Completed'),
        ('CANCELLED', 'Cancelled'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='PENDING')

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

class OrderItem(models.Model):
    # Model representing an item within an order
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} x {self.product.name}"
