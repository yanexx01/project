from django.contrib import admin
from .models import News
from modeltranslation.admin import TabbedTranslationAdmin


@admin.register(News)
class NewsAdmin(TabbedTranslationAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at',)
    search_fields = ('title', 'content', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('published_at',)
    ordering = ('-published_at',)
