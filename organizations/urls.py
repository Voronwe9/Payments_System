from django.urls import path

from .views import BalanceView

urlpatterns = [
    path(
        "<str:inn>/balance/",
        BalanceView.as_view(),
        name="organization-balance",
    ),
]
