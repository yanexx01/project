from django.urls import path
from .views import ListView

app_name = 'contacts'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
]
