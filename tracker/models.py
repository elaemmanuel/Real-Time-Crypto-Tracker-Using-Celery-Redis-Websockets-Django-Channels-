
from django.db import models

class Coin(models.Model):
    rank = models.IntegerField(null=True, blank=True)  
    name = models.CharField(max_length=100)
    symbol = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=8)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.symbol}): {self.price} (Rank: {self.rank})"

    class Meta:
        ordering = ['rank']