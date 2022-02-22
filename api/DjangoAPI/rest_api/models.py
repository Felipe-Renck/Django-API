from django.db import models
from django.contrib.gis.db import models
from djmoney.models.fields import MoneyField, CurrencyField

# Create your models here.
class Provider(models.Model):
    name = models.CharField(max_length = 100)
    email = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 100)
    language = models.CharField(max_length = 2, default='en')
    currency = CurrencyField(default='USD')

    def __str___(self):
        return self.name

class ServiceArea(models.Model):
    provider = models.ForeignKey(Provider)
    name = models.CharField(max_length=255)
    poly = models.PolygonField()
    price = MoneyField(max_digits=19, decimal_places=8)

    def __str__(self):
        return self.name