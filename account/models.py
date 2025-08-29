from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
# Role based access control model(RBAC)

class User(AbstractUser):
    ROLES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('cashier','Cashier'),
        ('waiter','Waiter'),
        ('staff', 'Staff'),
        ('customer', 'Customer'),
    )
    role = models.CharField(max_length=20, choices=ROLES, default='customer')

    # def __str__(self):
    #     return f"{self.username} ({self.role})"
    
    