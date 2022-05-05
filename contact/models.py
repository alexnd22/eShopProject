from django.db import models


class Contact(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=200)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
