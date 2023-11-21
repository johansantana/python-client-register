from django.db import models
from django.contrib.auth.models import AbstractUser

class ModifiedUser(AbstractUser):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=64)

    def __str__(self):
        return self.username