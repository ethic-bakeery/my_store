# from rest_framework.response import Response
# from rest_framework.decorators import api_view
# from django.shortcuts import get_object_or_404
# from .models import Delivery, Cart, User, Payment, Product, Order
# from .serializers import (
#     ProductSerializer, PaymentSerializer, UserSerializer,
#     DeliverySerializer, CartSerializer, OrderSerializer
# )
# from django.contrib.auth import authenticate
# from rest_framework.authentication import SessionAuthentication, BasicAuthentication
# from rest_framework.permissions import IsAuthenticated


# @api_view(['GET'])
# def getProducts(request):
#     products = Product.objects.all().order_by('-updated')
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getProduct(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     serializer = ProductSerializer(product, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def addToCart(request):
#     data = request.data
#     cart = Cart.objects.create(
#         product_id=data['product_id'],
#         quantity=data['quantity']
#     )
#     serializer = CartSerializer(cart, many=False)
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def deleteCart(request, pk):
#     cart_item = get_object_or_404(Cart, id=pk)
#     cart_item.delete()
#     return Response('Cart item has been deleted!')


# @api_view(['GET'])
# def getDeliveryAddresses(request):
#     delivery_addresses = Delivery.objects.all()
#     serializer = DeliverySerializer(delivery_addresses, many=True)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateDeliveryAddress(request, pk):
#     delivery_address = get_object_or_404(Delivery, id=pk)
#     serializer = DeliverySerializer(instance=delivery_address, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors)


# @api_view(['DELETE'])
# def deleteUser(request, pk):
#     user = get_object_or_404(User, id=pk)
#     user.delete()
#     return Response('User account has been deleted!')


# @api_view(['POST'])
# def registerUser(request):
#     data = request.data
#     user = User.objects.create_user(
#         username=data['username'],
#         password=data['password']
#     )
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def loginUser(request):
#     data = request.data
#     user = authenticate(username=data['username'], password=data['password'])
#     if user is not None:
#         serializer = UserSerializer(user, many=False)
#         return Response(serializer.data)
#     else:
#         return Response('Invalid credentials', status=400)


# @api_view(['GET'])
# def getUserProfile(request, pk):
#     user = get_object_or_404(User, id=pk)
#     serializer = UserSerializer(user, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateUserProfile(request, pk):
#     user = get_object_or_404(User, id=pk)
#     serializer = UserSerializer(instance=user, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)


# @api_view(['POST'])
# def placeOrder(request):
#     data = request.data
#     order = Order.objects.create(
#         product_id=data['product_id'],
#         quantity=data['quantity'],
#         user_id=request.user.id
#     )
#     serializer = OrderSerializer(order, many=False)
#     return Response(serializer.data)


# @api_view(['GET'])
# def getOrderHistory(request):
#     orders = Order.objects.filter(user_id=request.user.id)
#     serializer = OrderSerializer(orders, many=True)
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def cancelOrder(request, pk):
#     order = get_object_or_404(Order, id=pk)
#     order.delete()
#     return Response('Order has been cancelled!')


# @api_view(['POST'])
# def initiatePayment(request):
#     data = request.data
#     payment = Payment.objects.create(
#         amount=data['amount'],
#         payment_method=data['payment_method'],
#         user_id=request.user.id
#     )
#     serializer = PaymentSerializer(payment, many=False)
#     return Response(serializer.data)


# @api_view(['POST'])
# def createProduct(request):
#     data = request.data
#     product = Product.objects.create(
#         name=data['name'],
#         price=data['price']
#     )
#     serializer = ProductSerializer(product, many=False)
#     return Response(serializer.data)


# @api_view(['PUT'])
# def updateProduct(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     serializer = ProductSerializer(instance=product, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data)
#     return Response(serializer.errors, status=400)


# @api_view(['DELETE'])
# def deleteProduct(request, pk):
#     product = get_object_or_404(Product, id=pk)
#     product.delete()
#     return Response('Product has been deleted!')
