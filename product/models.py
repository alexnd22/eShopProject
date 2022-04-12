from django.contrib.auth.models import User
from django.db import models

from category.models import Category


class Product(models.Model):
    stock_choices = (('yes', 'Yes'), ('no', 'No'))

    name = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField(max_length=400, null=True, blank=True)
    active = models.BooleanField(default=True)
    price = models.IntegerField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    is_stock = models.CharField(max_length=10, choices=stock_choices, null=True, blank=True)
    release = models.DateField(null=True, blank=True)
    # email = models.EmailField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='media/', null=True, blank=True)

    def __str__(self):
        return self.name


class Cart(models.Model):
    STATUSES = (
        ('open', 'Open'),
        ('close', 'Close')
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=25, choices=STATUSES)

    def __str__(self):
        return f'{self.status} cart of {self.user}'


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.quantity} x {self.product.name} in {self.cart}'

    def get_total(self):
        return self.product.price * self.quantity
