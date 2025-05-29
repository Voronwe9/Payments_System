from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from organizations.models import Organization


class BalanceView(APIView):
    def get(self, request, inn):
        try:
            org = Organization.objects.get(inn=inn)
            return Response({"inn": inn, "balance": org.balance})
        except Organization.DoesNotExist:
            return Response(
                {"detail": "Organization not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
