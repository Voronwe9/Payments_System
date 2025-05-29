from django.db import models


class Organization(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    balance = models.DecimalField(
        max_digits=15, decimal_places=2, default=0.00
    )

    def __str__(self):
        return f"{self.inn} — {self.balance}"
