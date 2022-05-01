from django.contrib.auth.models import User, AbstractUser
from django.db import models


class UserExtend(User):
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=200)

    def __str__(self):
        return self.first_name
