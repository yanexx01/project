from django import template
from django.utils.translation import get_language
from django.urls import resolve, reverse

register = template.Library()


@register.simple_tag(takes_context=True)
def switch_lang(context, lang):
    """
    Switch language while preserving the current URL path.
    Usage: {% switch_lang 'en' %} or {% switch_lang 'ru' %}
    """
    request = context.get('request')
    if not request:
        return f'?lang={lang}'
    
    # Get current path without language prefix
    path = request.path
    current_lang = get_language()
    
    # Remove current language prefix if exists
    if path.startswith(f'/{current_lang}/'):
        path_without_lang = path[len(current_lang) + 1:]
    elif path.startswith('/en/') or path.startswith('/ru/'):
        # Handle explicit prefixes
        parts = path.split('/', 2)
        if len(parts) > 2:
            path_without_lang = '/' + parts[2] if parts[2] else ''
        else:
            path_without_lang = '/'
    else:
        path_without_lang = path
    
    # Ensure path starts with /
    if not path_without_lang.startswith('/'):
        path_without_lang = '/' + path_without_lang
    
    # Add new language prefix
    if lang == 'ru':
        # Russian is default, no prefix needed
        new_path = path_without_lang
    else:
        new_path = f'/{lang}{path_without_lang}'
    
    # Preserve query parameters
    if request.GET:
        query_params = request.GET.copy()
        query_params.pop('lang', None)
        if query_params:
            query_string = '&'.join(f'{k}={v}' for k, v in query_params.items())
            return f'{new_path}?{query_string}'
    
    return new_path


@register.simple_tag
def get_current_language():
    """Get the current language code."""
    return get_language()


@register.simple_tag
def is_active_lang(lang_code):
    """Check if the given language is currently active."""
    return get_language() == lang_code
