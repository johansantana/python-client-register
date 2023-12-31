from django.db import models
from users.models import ModifiedUser

class Client(models.Model):
    """This model holds the information of the client."""
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=20)
    email = models.CharField(max_length=64)
    username = models.CharField(max_length=32)
    date_added = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(ModifiedUser, on_delete=models.CASCADE)

    def __str__(self):
        """Return a string representation of the class"""
        return f"{self.first_name} {self.last_name}"
