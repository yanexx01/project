from django.contrib import admin
from .models import Debt


@admin.register(Debt)
class DebtAdmin(admin.ModelAdmin):
    list_display = ('account_number', 'last_name', 'address', 'amount', 'last_updated')
    list_filter = ('last_updated',)
    search_fields = ('account_number', 'last_name')
    ordering = ('-last_updated', 'account_number')

