from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from product.models import CartItem
from product.views import get_open_cart


class HomeTemplateView(TemplateView):
    template_name = 'home/home.html'


@login_required()
def open_cart_view(request):
    cart = get_open_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    return render(request, 'product/open_cart_view.html', {'cart_items': cart_items})


@login_required()
def checkout_view(request):
    cart = get_open_cart(request)
    cart_items = CartItem.objects.filter(cart=cart)
    for cart_item in cart_items:
        product = cart_item.product
        product.stock -= cart_item.quantity
        product.save()
    cart.status = 'closed'
    cart.save()
    # send_mail(subject='Contacted by website',
    #           message=f'Subject: {user.subject} \n'
    #                   f'Mail sent from: {user.email} \n'
    #                   f'Name: {user.name} \n'
    #                   f'Message: {user.message} \n',
    #           from_email=user.email,
    #           recipient_list=['alexwiky@gmail.com'])
    return redirect(reverse_lazy('homepage'))
