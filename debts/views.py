from django.views.generic import ListView
from debts.models import Debt
from news.models import News

class DebtListView(ListView):
    model = Debt
    template_name = 'debts/debts_list.html'
    context_object_name = 'debts_list'
    paginate_by = 10
    ordering = ['-last_updated', 'account_number']

    def get_queryset(self):
        account_number = self.request.GET.get('account_number', '').strip()
        last_name = self.request.GET.get('last_name', '').strip()

        # Ищем только если переданы оба параметра для защиты данных
        if account_number and last_name:
            return Debt.objects.filter(
                account_number=account_number,
                last_name__iexact=last_name # Точное, но регистронезависимое совпадение
            )
        
        # По умолчанию ничего не показываем
        return Debt.objects.none()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['account_number'] = self.request.GET.get('account_number', '')
        context['last_name'] = self.request.GET.get('last_name', '')
        # Флаг для шаблона, чтобы понимать, был ли поиск
        context['is_searched'] = bool(context['account_number'] or context['last_name'])
        
        context['latest_news'] = News.objects.all()[:2]
        return context

# class NewsDetailView(ListView):
#     model = News
#     template_name = 'debts/news_detail.html'
#     context_object_name = 'news_item'
#     slug_field = 'slug'
#     slug_url_kwarg = 'slug'