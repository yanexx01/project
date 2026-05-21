from django.contrib import admin
from .models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'full_name', 'amount', 'is_paid')
    list_filter = ('is_paid',)
    search_fields = ('account_number', 'full_name')
    ordering = ('-is_paid', 'account_number')
