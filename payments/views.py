from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment, BalanceLog
from organizations.models import Organization
from django.db import transaction

class BankWebhookView(APIView):
    def post(self, request):
        data = request.data
        operation_id = data.get("operation_id")

        if Payment.objects.filter(operation_id=operation_id).exists():
            return Response(status=status.HTTP_200_OK)

        with transaction.atomic():
            Payment.objects.create(**data)
            org, _ = Organization.objects.get_or_create(inn=data["payer_inn"])
            org.balance += data["amount"]
            org.save()
            BalanceLog.objects.create(organization=org, change_amount=data["amount"])
            print(f"Баланс организации {org.inn} обновлён на {data['amount']}")

        return Response(status=status.HTTP_200_OK)
