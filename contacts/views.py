from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'contacts/contacts_list.html'
