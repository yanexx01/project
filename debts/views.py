from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'debts/debts_list.html'
