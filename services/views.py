from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'services/services_list.html'
