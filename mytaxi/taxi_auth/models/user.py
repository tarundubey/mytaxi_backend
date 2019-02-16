from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    gender = models.CharField(max_length=5, null=True, blank=True, default=None)
    mobile=models.CharField(max_length=255)
    soft_delete=models.BooleanField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def get_name(self):
        name = self.first_name + " " + self.last_name
        if len(name.strip()) != 0:
            return name
        return self.username

