from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from django.views.generic import CreateView, ListView, UpdateView, DeleteView, DetailView

from category.forms import CategoryForm, CategoryFormUpdate
from category.models import Category


class CategoryCreateView(CreateView):
    template_name = 'category/create_category.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('list_of_categories')
    # permission_required = 'category.add_category'


class CategoryListView(ListView):
    template_name = 'category/list_of_categories.html'
    model = Category
    context_object_name = 'all_categories'
    # permission_required = 'category.view_category'


class CategoryUpdateView(UpdateView):
    template_name = 'category/update_category.html'
    model = Category
    form_class = CategoryFormUpdate
    success_url = reverse_lazy('list_of_categories')
    # permission_required = 'category.change_category'


class CategoryDeleteView(DeleteView):
    template_name = 'category/delete_category.html'
    model = Category
    success_url = reverse_lazy('list_of_categories')
    # permission_required = 'category.delete_category'


# @login_required()
# @permission_required('category.delete_category_by_popup')
def delete_category_with_popup(request, pk):
    current_category = Category.objects.filter(id=pk)
    current_category.delete()
    return redirect('list_of_categories')


class CategoryDetailView(DetailView):
    template_name = 'category/detail_category.html'
    model = Category
    # permission_required = 'category.view_category'


# @login_required()
# @permission_required('category.detail_category_by_popup')
def details_category_with_popup(request, pk):
    current_details_category = Category.objects.get(id=pk)
    return render(request, 'category/list_of_categories.html', current_details_category)
