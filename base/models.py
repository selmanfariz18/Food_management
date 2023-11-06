from django.db import models
from django.contrib.auth.models import AbstractUser, User

# Create your models here.

choices = (
    ('normal_user', 'normal_user'),
    ('community', 'community'),
    ('hotel', 'hotel'),
)


class base_models(models.Model):
    '''model which is connected with User model, contain data about the user type.'''
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=15, choices=choices, null=True)
    address = models.CharField(max_length=100, null=True)
    hotel_license = models.CharField(max_length=20, null=True)

    def __str__(self):
        return self.user.username