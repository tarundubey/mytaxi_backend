from django.contrib.auth.models import Group
from django.db import models

class Role(Group):
    role_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'role'
        verbose_name_plural = 'Roles'