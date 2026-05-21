from django.urls import path
from .views import ListView, CreateView

app_name = 'applications'

urlpatterns = [
    path('', ListView.as_view(), name='list'),
    path('create/', CreateView.as_view(), name='create'),
]
