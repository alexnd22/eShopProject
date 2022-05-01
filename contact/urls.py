from django.urls import path
from contact import views

urlpatterns = [
    path('contact-form/', views.ContactCreateView.as_view(), name='contact-form'),
    path('confirm/', views.ContactTemplateView.as_view(), name='confirm'),
]
