from django.db import models

from django.db import models

class Organization(models.Model):
    inn = models.CharField(max_length=12, unique=True)
    balance = models.BigIntegerField(default=0)

    def __str__(self):
        return f"{self.inn} — {self.balance}"
