from django.urls import path
from .views import DebtListView

app_name = 'debts'

urlpatterns = [
    path('', DebtListView.as_view(), name='list'),
]
