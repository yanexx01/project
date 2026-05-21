from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'applications/application_list.html'


class CreateView(TemplateView):
    template_name = 'applications/application_form.html'
