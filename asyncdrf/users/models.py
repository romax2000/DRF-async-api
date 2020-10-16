from django.db import models

# Create your models here.


class Item(models.Model):
    code = models.CharField(max_length=8, unique=True)
    name = models.CharField(max_length=128, unique=True)
    actual_price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
