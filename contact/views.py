from django.core.mail import send_mail
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from alexndProject.settings import EMAIL_HOST_USER
from contact.forms import ContactForm
from contact.models import Contact


class ContactCreateView(CreateView):
    template_name = 'contact/create_contact_form.html'
    model = Contact
    form_class = ContactForm

    def form_valid(self, form):
        if form.is_valid() and not form.errors:
            contact_form = form.save(commit=False)
            contact_form.save()
            send_mail(contact_form.subject, contact_form.message, from_email=contact_form.email,
                      recipient_list=[EMAIL_HOST_USER])
            return redirect(reverse_lazy('confirm'))


class ContactTemplateView(TemplateView):
    template_name = 'contact/confirm_contact.html'
