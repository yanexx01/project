from django.views.generic import TemplateView


class ListView(TemplateView):
    template_name = 'news/news_list.html'
