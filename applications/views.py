from django.views.generic import ListView, CreateView, TemplateView
from django.urls import reverse_lazy
from applications.models import Application
from services.models import Service


class ApplicationListView(ListView):
    model = Application
    template_name = 'applications/application_list.html'
    context_object_name = 'applications_list'
    paginate_by = 10
    ordering = ['-created_at']


class ApplicationCreateView(CreateView):
    model = Application
    template_name = 'applications/application_form.html'
    fields = ['application_type', 'service', 'name', 'phone', 'email', 'message']
    success_url = reverse_lazy('applications:success')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['services'] = Service.objects.all()
        return context


class ApplicationSuccessView(TemplateView):
    template_name = 'applications/application_success.html'
