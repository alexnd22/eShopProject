from django import forms
from django.forms import TextInput, Textarea, HiddenInput

from category.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'active']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter category name', 'class': 'form-control'}),
            'description': Textarea(attrs={'placeholder': 'Please enter category description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CategoryForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Your name'
        # self.fields['name'].widget = HiddenInput()

    def clean(self):
        cleaned_data = self.cleaned_data
        name_input = self.cleaned_data.get('name')
        all_categories = Category.objects.all()
        for category in all_categories:
            if name_input == category.name:
                msg = 'This name already exist in db!'
                self._errors['name'] = self.error_class([msg])

        return cleaned_data


class CategoryFormUpdate(forms.ModelForm):
    class Meta:
        model = Category
        # fields = '__all__'
        fields = ['name', 'description', 'active']
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Please enter category name', 'class': 'form-control'}),
            'description': Textarea(
                attrs={'placeholder': 'Please enter category description', 'class': 'form-control'})
        }

    def __init__(self, *args, **kwargs):
        super(CategoryFormUpdate, self).__init__(*args, **kwargs)
        self.fields['name'].label = 'Your name'
        # self.fields['name'].widget = HiddenInput()
