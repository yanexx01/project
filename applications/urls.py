from django.urls import path
from .views import ApplicationListView, ApplicationCreateView, ApplicationSuccessView

app_name = 'applications'

urlpatterns = [
    # path('', ApplicationListView.as_view(), name='list'),
    path('', ApplicationCreateView.as_view(), name='create'),
    path('success/', ApplicationSuccessView.as_view(), name='success'),
]
