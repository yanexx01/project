from django.urls import path
from .views import ApplicationListView, ApplicationCreateView

app_name = 'applications'

urlpatterns = [
    path('', ApplicationListView.as_view(), name='list'),
    path('create/', ApplicationCreateView.as_view(), name='create'),
]
