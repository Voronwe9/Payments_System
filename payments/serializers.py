from rest_framework import serializers

class PaymentWebhookSerializer(serializers.Serializer):
    operation_id = serializers.CharField()
    payer_inn = serializers.CharField()
    amount = serializers.FloatField()