from django.urls import path

from home import views

urlpatterns = [
    path('', views.HomeTemplateView.as_view(), name='homepage'),
    path('open-cart-view/', views.open_cart_view, name='open_cart_view'),
    path('checkout/', views.checkout_view, name='checkout')
]
