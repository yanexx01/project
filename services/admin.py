from django.contrib import admin
from .models import ServiceCategory, Service


@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug')
    search_fields = ('title',)
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('title',)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'price', 'created_at')
    list_filter = ('category', 'created_at')
    search_fields = ('title', 'description', 'category__title')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('created_at',)
    ordering = ('-created_at',)
