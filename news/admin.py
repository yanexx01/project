from django.contrib import admin
from .models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'published_at')
    list_filter = ('published_at',)
    search_fields = ('title', 'content', 'short_description')
    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('published_at',)
    ordering = ('-published_at',)
