from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.models import Category
from product.forms import ProductForm
from product.models import Product, Cart, CartItem


class ProductCreateView(CreateView):
    template_name = 'product/create_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list_of_products')
    # permission_required = 'product.add_product'


class ProductListView(ListView):
    template_name = 'product/list_of_products.html'
    model = Product
    context_object_name = 'all_products'


class ProductUpdateView(UpdateView):
    template_name = 'product/update_product.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('list_of_products')
    # permission_required = 'product.change_product'


class ProductDeleteView(DeleteView):
    template_name = 'product/delete_product.html'
    model = Product
    success_url = reverse_lazy('list_of_products')
    # permission_required = 'product.delete_product'


def delete_product_with_popup(request, pk):
    current_product = Product.objects.filter(id=pk)
    current_product.delete()
    return redirect('list_of_products')


class ProductDetailView(DetailView):
    template_name = 'product/detail_product.html'
    model = Product
    # permission_required = 'product.view_product'


def details_product_with_popup(request, pk):
    current_details_product = Product.objects.get(id=pk)
    return render(request, 'product/list_of_products.html', current_details_product)


def get_products_per_category(request, pk):
    products_per_category = Product.objects.filter(category_id=pk)
    get_category = Category.objects.get(id=pk)
    return render(request, 'product/products_per_category.html',
                  {'products_per_category': products_per_category, 'name_of_category': get_category})


def get_open_cart(request):
    open_carts = Cart.objects.filter(user=request.user, status='open')
    if open_carts.count() > 0:
        return open_carts.first()
    else:
        return Cart.objects.create(user=request.user, status='open')


@login_required(login_url='/login/')
def add_products_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST.get('product_id')
        quantity = int(request.POST.get('quantity', 1))
        cart = get_open_cart(request)
        existing_cart_items = CartItem.objects.filter(cart=cart, product=product_id)
        if existing_cart_items.count() > 0:
            cart_item = existing_cart_items.first()
            cart_item.quantity += quantity
            cart_item.save()
        else:
            CartItem.objects.create(cart=cart, product_id=product_id, quantity=quantity)
        return redirect(request.META['HTTP_REFERER'])
    else:
        return redirect('list_of_products')
