from django.urls import path
from .views import ListView

app_name = 'services'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
]
