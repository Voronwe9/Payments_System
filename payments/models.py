from django.db import models
from organizations.models import Organization

class Payment(models.Model):
    operation_id = models.UUIDField(unique=True)
    amount = models.BigIntegerField()
    payer_inn = models.CharField(max_length=12)
    document_number = models.CharField(max_length=50)
    document_date = models.DateTimeField(auto_now_add=False)
    created_at = models.DateTimeField(auto_now_add=True)

class BalanceLog(models.Model):
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    change_amount = models.BigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
