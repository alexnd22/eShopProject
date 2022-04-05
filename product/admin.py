from django.contrib import admin

from product.models import Product, Cart, CartItem

admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(CartItem)
