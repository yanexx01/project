from django.views.generic import ListView, DetailView
from services.models import Service


class ServiceListView(ListView):
    model = Service
    template_name = 'services/services_list.html'
    context_object_name = 'services_list'
    paginate_by = 10
    ordering = ['-created_at']


class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем другие услуги для sidebar
        context['latest_services'] = Service.objects.exclude(pk=self.object.pk)[:5]
        return context
