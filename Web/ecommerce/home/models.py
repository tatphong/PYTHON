from django.db import models
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