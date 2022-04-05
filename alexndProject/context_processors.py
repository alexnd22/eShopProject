from category.models import Category
from product.models import CartItem
from product.views import get_open_cart


def get_all_categories(request):
    all_categories = Category.objects.all()
    return {'allcategories': all_categories}


def navbar_data(request):
    if request.user.is_authenticated:
        cart = get_open_cart(request)
        cart_items = CartItem.objects.filter(cart=cart)
        count = sum([c.quantity for c in cart_items])
    else:
        count = 0
    return {'categories': Category.objects.all(), 'cart_items_count': count}
