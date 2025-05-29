from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Payment, BalanceLog
from organizations.models import Organization
from django.db import transaction
from .serializers import PaymentWebhookSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

class BankWebhookView(APIView):
    @swagger_auto_schema(
        request_body=PaymentWebhookSerializer,
        responses={201: openapi.Response("Created")},
        operation_description="Приём вебхука от банка. Создаёт платёж и обновляет баланс организации.",
    )
    def post(self, request):
        serializer = PaymentWebhookSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        data = serializer.validated_data
        operation_id = data["operation_id"]

        if Payment.objects.filter(operation_id=operation_id).exists():
            return Response(
                {"detail": f"Payment with operation_id '{operation_id}' already exists."},
                status=status.HTTP_200_OK
            )

        with transaction.atomic():
            payment = Payment.objects.create(**data)
            org, _ = Organization.objects.get_or_create(inn=data["payer_inn"])
            org.balance += data["amount"]
            org.save()
            BalanceLog.objects.create(organization=org, change_amount=data["amount"])
            print(f"Баланс организации {org.inn} обновлён на {data['amount']}")

        return Response(status=status.HTTP_201_CREATED)
