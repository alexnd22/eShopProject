from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render
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
