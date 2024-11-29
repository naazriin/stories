from django.db import models
from django.contrib.auth.models import AbstractUser

from django.contrib.auth import get_user_model

User = get_user_model()



# class User(AbstractUser):
#     photo = models.ImageField(upload_to='users', blank=True, null=True)
#     bio = models.TextField(blank=True, null=True)


class BlackListedIPAddress(models.Model):
    ip_address = models.GenericIPAddressField()

    def __str__(self):
        return self.ip_address
    

    class Meta:
        verbose_name = 'Black Listed IP'
        verbose_name_plural = 'Black Listed IPs'