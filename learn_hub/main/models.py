from django.db import models
from django.contrib.auth.models import User
from django.db import models

class Course(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.title

class Mentor(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    approved = models.BooleanField(default=False)

    def str(self):
        return self.name

class Admin(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def str(self):
        return self.name
    

class Profile(models.Model):
    USER_ROLES = (
        ('admin', 'Admin'),
        ('user', 'User'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLES, default='user')

    def __str__(self):
        return self.user.username