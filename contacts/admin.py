from django.contrib import admin
from .models import ContactInfo


@admin.register(ContactInfo)
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone', 'email', 'address')
    search_fields = ('phone', 'email', 'address')

    def has_add_permission(self, request):
        # Разрешить создание только одной записи
        if self.model.objects.exists():
            return False
        return True

    def has_delete_permission(self, request, obj=None):
        # Запретить удаление, чтобы всегда была хотя бы одна запись
        if self.model.objects.count() > 1:
            return True
        return False
