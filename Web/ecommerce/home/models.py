from django.db import models
# from django.db import connection

# Create your models here.

class ProductExample(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=150)
    price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'product_example'