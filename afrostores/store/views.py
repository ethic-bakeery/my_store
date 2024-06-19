from django.http import response
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework import status
from django.shortcuts import render
from django.http import HttpRequest
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.serializers import Serializer
from .models import Payment,User,Delivery,Cart,Product
from django.http import response
from .serializers import ProductSerializer,DeliverySerializer,CartSerializer,PaymentSerializer,UserSerializer
from store import serializers
from django.shortcuts import get_object_or_404

from .utils import (
    getProducts, 
    getProduct, 
    addToCart, 
    deleteCart, 
    getDeliveryAddresses, 
    updateDeliveryAddress, 
    deleteUser, 
    registerUser, 
    loginUser, 
    getUserProfile, 
    updateUserProfile, 
    placeOrder, 
    getOrderHistory, 
    cancelOrder, 
    initiatePayment, 
    createProduct, 
    updateProduct, 
    deleteProduct
)


@api_view(['GET']) #Aabuu make sure you after testing you disabled those functionalities
def getRoutes(request):
    routes = [
        
        {
            'Endpoint': '/products',
            'method': 'GET',
            'body': None,
            'description': 'Display available products'
        },
        {
            'Endpoint': '/product/id',
            'method': 'GET',
            'body': None,
            'description': 'Returns a single product object'
        },
        {
            'Endpoint': '/cart/add',
            'method': 'POST',
            'body': {'product_id': "", 'quantity': ""},
            'description': 'Add a product to the cart'
        },
        {
            'Endpoint': '/cart/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete an item from the cart'
        },
        {
            'Endpoint': '/user/delivery-address/id',
            'method': 'GET',
            'body': None,
            'description': 'Get user delivery address'
        },
         {
            "Endpoint": "/user/update_delivery-address/<id>",
            "method": "PUT",
            "body": {
                "firstname": "string",
                "lastname": "string",
                "country": "string",
                "state": "string",
                "city": "string",
                "postal_code": "integer",
                "contact": "string"
            },
              "description": "Update user delivery address"
            },
         {
            'Endpoint': '/user/delete/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Delete user account'
        },
         {
            'Endpoint': '/register',
            'method': 'POST',
            'body': {'username': "", 'password': ""},
            'description': 'Register a new user'
        },
        {
            'Endpoint': '/login',
            'method': 'POST',
            'body': {'username': "", 'password': ""},
            'description': 'User login'
        },
        {
            'Endpoint': '/profile/id',
            'method': 'GET',
            'body': None,
            'description': 'Get user profile'
        },
        {
            'Endpoint': '/update/profile/id',
            'method': 'PUT',
            'body': {'name': "", 'email': "","password":""},
            'description': 'Update user profile'
        },
        {
            'Endpoint': '/order',
            'method': 'POST',
            'body': {'product_id': "", 'quantity': 1},
            'description': 'Place a new order'
        },
        {
            'Endpoint': '/orders',
            'method': 'GET',
            'body': None,
            'description': 'Get user order history'
        },
        {
            'Endpoint': '/order/id',
            'method': 'DELETE',
            'body': None,
            'description': 'Cancel an order'
        },
        {
            'Endpoint': '/payment',
            'method': 'POST',
            'body': {'amount': "", 'payment_method': ""},
            'description': 'Initiate a payment'
        },
        # {
        #     'Endpoint': '/payment/callback',
        #     'method': 'POST',
        #     'body': {'payment_id': "", 'status': ""},
        #     'description': 'Handle payment callback'
        # },
        {
            'Endpoint': '/admin/products/',
            'method': 'GET',
            'body': None,
            'description': 'Display available products'
        },
       
         {
            'Endpoint': '/admin/product/id',
            'method': 'GET',
            'body': None,
            'description': 'Delete a product (admin)'
        },
         {
            'Endpoint': '/admin/update_product/id',
            'method': 'PUT',
            'body': {'name': "", 'price': ""},
            'description': 'Update a product (admin)'
        },
         {
            'Endpoint': '/admin/delete_product/id',
            'method': 'DELETE',
            'body': {'name': "", 'price': ""},
            'description': 'Update a product (admin)'
        },

        {
            "Endpoint": "/admin/create_product",
            "method": "POST",
            "body": {
                "name": "Product Name",
                "description": "Product description",
                "price": 100,
                "instructions": "Usage instructions",
                "sold_out": False
        },
           "description": "Create a new product (admin)"
        }

    ]
    return Response(routes)


@api_view(['GET'])
def getProducts(request):
    product = Product.objects.all()
    serializer = ProductSerializer(product, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getProduct(request, pk):
    product = get_object_or_404(Product, pk=pk)
    serializer = ProductSerializer(product)
    return Response(serializer.data)

@api_view(['POST'])
def addToCart(request):
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def deleteCart(request, pk): # have not tested due to ssrf token
    try:
        cart_item = Cart.objects.get(pk=pk)
    except Cart.DoesNotExist:
        return Response({'error': 'Cart item not found'}, status=status.HTTP_404_NOT_FOUND)
    
    cart_item.delete()
    return Response({'message': 'Cart item deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def getDelivery(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    serializer = DeliverySerializer(delivery)
    return Response(serializer.data)

@api_view(['PUT'])
def updateDelivery(request, pk):
    delivery = get_object_or_404(Delivery, pk=pk)
    data = request.data.copy()
    if 'user_profile' not in data:
        data['user_profile'] = delivery.user_profile.id
    
    serializer = DeliverySerializer(instance=delivery, data=data, partial=True)
    
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
def deleteUser(request, pk): # tested, it works 
    UseR = User.objects.get(id=pk)
    UseR.delete()
    return Response('User has been deleted!')


@api_view(['GET'])
def getUserProfile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user)
    return Response(serializer.data)

@api_view(['PUT'])
def updateUserProfile(request, pk):
    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return Response({'error': 'User not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = UserSerializer(user, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def placeOrderView(request):
#     return placeOrder(request)

# @api_view(['GET'])
# def getOrderHistoryView(request):
#     return getOrderHistory(request)

# @api_view(['DELETE'])
# def cancelOrderView(request, pk):
#     return cancelOrder(request, pk)

# @api_view(['POST'])
# def initiatePaymentView(request):
#     return initiatePayment(request)

@api_view(['POST'])
def createProduct(request):
    serializer = ProductSerializer(data=request.data)
    
    if serializer.is_valid():
        product = serializer.save()
        return Response(serializer.data, status=201) 
    else:
        return Response(serializer.errors, status=400)

@api_view(['PUT'])
def updateProduct(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

def deleteProduct(request, pk): # have not tested
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response({'message': 'Product deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def registerUser(request):
    data = request.data
    if 'username' not in data or 'password' not in data or 'email' not in data:
        return Response({'error': 'Username, password, and email are required.'}, status=400)
    
    username = data['username']
    email = data['email']
    password = data['password']

    if User.objects.filter(username=username).exists():
        return Response({'error': 'Username already exists.'}, status=400)
    if User.objects.filter(email=email).exists():
        return Response({'error': 'Email address already registered.'}, status=400)

    else:
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email
        )
        user.save()
    

@api_view(['POST'])
def loginUser(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)
    
    if user is not None:
        login(request._request, user)  
        return Response({'message': 'Login successful'})
    else:
        return Response({'error': 'Invalid credentials'}, status=400)
