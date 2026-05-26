from django.views.generic import ListView, DetailView
from news.models import News


class NewsListView(ListView):
    model = News
    template_name = 'news/news_list.html'
    context_object_name = 'news_list'
    paginate_by = 9
    ordering = ['-published_at']


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
