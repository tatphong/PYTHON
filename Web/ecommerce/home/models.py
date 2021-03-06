from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _
from .managers import CustomUserManager
# from django.db import connection

# Create your models here.

class ProductExample(models.Model):
    name = models.CharField(max_length=150)
    price = models.IntegerField()
    image = models.ImageField()

    class Meta:
        managed = False
        db_table = 'product_example'

    def __str__(self):
        return self.name

class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email