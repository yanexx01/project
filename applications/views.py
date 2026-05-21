from django.views.generic import ListView, CreateView
from django.urls import reverse_lazy
from applications.models import Application


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
    success_url = reverse_lazy('applications:application_list')
