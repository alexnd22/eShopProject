import django_filters

from category.models import Category


class CategoryFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['name', 'active']

    def __init__(self, *args, **kwargs):
        super(CategoryFilter, self).__init__(*args, **kwargs)
        self.filters['name'].field.widget.attrs.update({'class': 'form-control',  'placeholder': 'Please enter name'})
        self.filters['active'].field.widget.attrs.update({'class': 'form-control'})

