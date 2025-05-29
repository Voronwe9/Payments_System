from rest_framework import serializers
from .models import Payment

class PaymentWebhookSerializer(serializers.Serializer):
    operation_id = serializers.UUIDField()
    amount = serializers.DecimalField(max_digits=12, decimal_places=2)
    payer_inn = serializers.CharField(max_length=12)
    document_number = serializers.CharField(max_length=100)
    document_date = serializers.DateTimeField()