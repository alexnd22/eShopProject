import django_filters

from product.models import Product


class ProductFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price = django_filters.NumberFilter(lookup_expr='icontains')

    class Meta:
        model = Product
        fields = ['name', 'price', 'category']

    def __init__(self, *args, **kwargs):
        super(ProductFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter name'})
        self.filters['price'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter price'})
        self.filters['category'].field.widget.attrs.update({'class': 'form-control'})


class ProductPerCategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')
    price__gte = django_filters.NumberFilter(field_name='price', lookup_expr='gte')
    price__lte = django_filters.NumberFilter(field_name='price', lookup_expr='lte')

    class Meta:
        model = Product
        fields = ['name', 'price__gte', 'price__lte']

    def __init__(self, *args, **kwargs):
        super(ProductPerCategoryFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control', 'placeholder': 'Please enter name'})
        self.filters['price__gte'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter price'})
        self.filters['price__lte'].field.widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Please enter price'})
