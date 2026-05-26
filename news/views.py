from django.views.generic import ListView, DetailView
from news.models import News
from django.http import HttpRequest


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 10
    ordering = ['-published_at']

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем параметры GET для пагинации (кроме page)
        request = self.request
        get_params = '&' + request.GET.urlencode() if request.GET else ''
        # Удаляем параметр page из get_params, если он есть
        if 'page' in request.GET:
            params = request.GET.copy()
            params.pop('page', None)
            get_params = '&' + params.urlencode() if params else ''
        context['get_params'] = get_params
        return context


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news_detail.html'
    context_object_name = 'news'
    slug_field = 'slug'
    slug_url_kwarg = 'slug'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем последние новости для sidebar
        context['latest_news'] = News.objects.exclude(pk=self.object.pk)[:5]
        return context
