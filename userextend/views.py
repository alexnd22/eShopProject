from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView

from alexndProject.settings import EMAIL_HOST_USER
from userextend.forms import UserExtendForm, UserExtendUpdateForm
from userextend.models import UserExtend


class UserExtendCreateView(CreateView):
    template_name = 'userextend/create_user.html'
    model = UserExtend
    form_class = UserExtendForm
    success_url = reverse_lazy('homepage')

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            user = form.save(commit=False)
            message = f"Your username is {user.username} and your password is {form.cleaned_data['password1']}"
            send_mail('Create a new user', message, from_email=EMAIL_HOST_USER, recipient_list=[user.email])
            user.save()
            get_group = Group.objects.get(name='Clients')
            get_group.user_set.add(user.id)
        return redirect('login')


class UserExtendUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'userextend/update_user.html'
    model = UserExtend
    form_class = UserExtendUpdateForm
    success_url = reverse_lazy('homepage')

    def get_queryset(self):
        return UserExtend.objects.filter(user_ptr_id=self.request.user.id)
