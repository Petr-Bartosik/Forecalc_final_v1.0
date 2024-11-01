
from django.db import models
from django.contrib.auth.models import User
from decimal import Decimal


class DrevoZaznam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nazev = models.CharField(max_length=100)
    delka = models.DecimalField(max_digits=5, decimal_places=2)
    prumer = models.DecimalField(max_digits=5, decimal_places=2)
    objem = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def save(self, *args, **kwargs):
        # Převedeme průměr z cm na metry
        prumer_v_metrech = self.prumer * Decimal('0.01')
        # Vypočítáme objem
        self.objem = (self.delka * (prumer_v_metrech ** 2) * Decimal('3.14')) / Decimal('4')
        super().save(*args, **kwargs)

from django.db import models

class WoodVolume(models.Model):
    length = models.FloatField()
    diameter = models.FloatField()
    volume = models.FloatField()

    def __str__(self):
        return f"Length: {self.length}, Diameter: {self.diameter}, Volume: {self.volume}"
