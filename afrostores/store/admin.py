# admin.py
from django.contrib import admin
from .models import Delivery, Product, ProductImage, Payment, Cart, Order

admin.site.register(Delivery)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Payment)
admin.site.register(Cart)
admin.site.register(Order)
