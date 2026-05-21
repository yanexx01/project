from django.urls import path
from .views import ListView

app_name = 'debts'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
]
