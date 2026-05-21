from django.views.generic import ListView
from services.models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services_list'
    paginate_by = 10
    ordering = ['-created_at']
