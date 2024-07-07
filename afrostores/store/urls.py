from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, DeliveryViewSet, ProductViewSet, ProductImageViewSet, PaymentViewSet, CartViewSet, OrderViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'deliveries', DeliveryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'product-images', ProductImageViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
