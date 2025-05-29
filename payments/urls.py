from django.urls import path
from .views import BankWebhookView

urlpatterns = [
    path('webhook/bank/', BankWebhookView.as_view(), name='webhook-bank'),
]