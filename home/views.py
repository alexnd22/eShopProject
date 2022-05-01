from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from alexndProject.settings import EMAIL_HOST_USER
from product.models import CartItem
from product.views import get_open_cart
from userextend.models import UserExtend


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
    list_with_products = []
    all_products = ''
    for cart_item in cart_items:
        list_with_products.append(cart_item.product.name)
        product = cart_item.product
        product.quantity -= cart_item.quantity
        product.save()
    cart.status = 'closed'
    cart.save()
    for product in list_with_products:
        all_products += f'{product}; '
    message = f'Dear {request.user.first_name} {request.user.last_name}, your order has been confirmed and' \
              f' will be delivered to your address {UserExtend.objects.get(user_ptr_id=request.user.id).address}.\n\n\n ' \
              f'The ordered products are: {all_products}'
    send_mail('Order confirmation', message, from_email=EMAIL_HOST_USER, recipient_list=[request.user.email])

    return redirect(reverse_lazy('success_order'))
