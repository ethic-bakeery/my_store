from rest_framework.serializers import ModelSerializer
from .models import Product, Delivery, Payment, Cart,User,Order
from store import serializers

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class DeliverySerializer(serializers.ModelSerializer):
    class Meta:
        model = Delivery
        fields = '__all__'
        extra_kwargs = {
            'user_profile': {'required': False}
        }

class PaymentSerializer(ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class CartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        extra_kwargs = {
            'password': {'write_only': True},  # Ensure password is write-only
        }
class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'
