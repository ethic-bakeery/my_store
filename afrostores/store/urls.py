from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name='routes'),

    path('products/', views.getProducts, name='products'),
    path('product/<str:pk>/', views.getProduct, name='product'),

    path('cart/add', views.addToCart, name='add-to-cart'),
    path('cart/delete/<str:pk>/', views.deleteCart, name='delete-cart'),

    path('delivery-address/<str:pk>/', views.getDelivery, name='get-delivery-address'),
    path('update_delivery-address/<str:pk>/', views.updateDelivery, name='update_delivery-address'),


    path('delete/<str:pk>', views.deleteUser, name='delete-user'),
    path('register/', views.registerUser, name='register-user'),
    path('login/', views.loginUser, name='login-user'),
    path('profile/<str:pk>', views.getUserProfile, name='get-user-profile'),
    path('update/profile/<str:pk>', views.updateUserProfile, name='update-user-profile'),

    # path('order/', views.placeOrderView, name='place-order'),
    # path('orders/', views.getOrderHistoryView, name='get-order-history'),
    # path('order/<str:pk>/cancel/', views.cancelOrderView, name='cancel-order'),

    # path('payment/', views.initiatePaymentView, name='initiate-payment'),
    path('admin/products/', views.getProducts, name='products'),
    path('admin/create_product/', views.createProduct, name='create_product'),
    path('admin/update_product/<str:pk>/', views.updateProduct, name='update-product'),
    path('admin/delete_product/<str:pk>/', views.deleteProduct, name='delete-product'),
]
