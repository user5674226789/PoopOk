from django.contrib.auth.models import AbstractUser
from cloudinary.models import CloudinaryField
from django.db import models


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=10, blank=True, null=True, verbose_name='Мобільний номер')
    image = CloudinaryField('user_images', blank=True, null=True)

    class Meta:
        db_table = 'user'
        verbose_name = 'Користувача'
        verbose_name_plural = 'Користувач'

    def __str__(self):
        return self.username
