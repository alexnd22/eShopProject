from django.urls import path

from userextend import views

urlpatterns = [
    path('create-user/', views.UserExtendCreateView.as_view(), name='create_user'),
    path('update-user/<int:pk>/', views.UserExtendUpdateView.as_view(), name='update_user')
]
