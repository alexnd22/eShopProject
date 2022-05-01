"""alexndProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views
from django.contrib.auth.views import LoginView
from django.urls import path, include

from userextend.forms import AuthenticationLoginForm, SetPasswordCustomForm, PasswordResetCustomForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('', include('category.urls')),
    path('', include('product.urls')),
    path('', include('userextend.urls')),
    path('', include('contact.urls')),
    path('login/', LoginView.as_view(authentication_form=AuthenticationLoginForm), name="login"),
    path("reset/<uidb64>/<token>/", views.PasswordResetConfirmView.as_view(form_class=SetPasswordCustomForm),
         name="password_reset_confirm"),
    path("password_reset/", views.PasswordResetView.as_view(form_class=PasswordResetCustomForm), name="password_reset"),
    path('', include('django.contrib.auth.urls')),
]
