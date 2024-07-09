from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(max_length=255, unique=True)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    def __str__(self):
        return self.username
    
class Delivery(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=255, null=True)
    lastname = models.CharField(max_length=255, null=True)
    country = models.CharField(max_length=255, null=True)
    state = models.CharField(max_length=255, null=True)
    city = models.CharField(max_length=255, null=True)
    postal_code = models.IntegerField(null=True)
    contact = models.CharField(max_length=255, null=True)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"

class Product(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)
    price = models.IntegerField(null=True)
    instructions = models.TextField(null=True)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class ProductImage(models.Model):
    product = models.ForeignKey(Product, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='media/uploads/images', null=True)

    def __str__(self):
        return self.product.name + ' Image'

class Payment(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    made_on = models.DateTimeField(auto_now_add=True, null=True)
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Payment for {self.user_profile.username}"

class Cart(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"Cart for {self.user_profile.username}"

class Order(models.Model):
    user_profile = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=True)
    quantity = models.IntegerField(default=1)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order for {self.user_profile.username}"