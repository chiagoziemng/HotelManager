from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    # Additional fields for the custom user model
    ROLES_CHOICES = (
        ('front_desk_manager', 'Front Desk Manager'),
        ('auditor', 'Auditor'),
        ('manager', 'Manager'),
        ('general_manager', 'General Manager'),
        ('supervisor', 'Supervisor'),
        ('owner', 'Owner'),
        ('bar_staff', 'Bar_staff'),

    )
    roles = models.CharField(max_length=20, choices=ROLES_CHOICES)

    # Add any other fields you need for your user model

    def __str__(self):
        return self.username


