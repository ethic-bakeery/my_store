
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import Register, Login, Logout, DeleteUser,Users, UpdateUser, Delivery, Product, ProductImage, Payment, Cart, Order
from django.urls import path

router = DefaultRouter()
router.register(r'users', Users)
router.register(r'deliveries', Delivery, basename='delivery')
router.register(r'products', Product, basename='product')
router.register(r'product-images', ProductImage, basename='productimage')
router.register(r'payments', Payment, basename='payment')
router.register(r'carts', Cart, basename='cart')
router.register(r'orders', Order, basename='order')
# router.register(r'Users', Users, basename='users')

urlpatterns = [
    path('register/', Register.as_view(), name='register'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('users/<int:id>/delete/', DeleteUser.as_view(), name='delete-user'),
    path('users/<int:id>/update/', UpdateUser.as_view(), name='update-user'),
    path('register/', Register.as_view(), name='register'),
    path('', include(router.urls)),
]
