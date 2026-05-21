from django.views.generic import ListView
from debts.models import Debt


class DebtListView(ListView):
    model = Debt
    template_name = 'debts/debts_list.html'
    context_object_name = 'debts_list'
    paginate_by = 10
    ordering = ['-is_paid', 'account_number']
