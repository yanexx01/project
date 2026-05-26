"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.utils.translation import gettext_lazy as _

# Language-prefixed URL patterns
lang_prefixes = {
    'ru': '',  # Default language has no prefix
    'en': 'en/',
}

# Create language-specific urlpatterns
def create_lang_urlpatterns():
    urlpatterns = []
    
    # Default language (Russian) - no prefix
    urlpatterns.extend([
        path('', include('home.urls')),
        path('services/', include('services.urls')),
        path('news/', include('news.urls')),
        path('applications/', include('applications.urls')),
        path('debts/', include('debts.urls')),
        path('contacts/', include('contacts.urls')),
    ])
    
    # English with prefix
    urlpatterns.extend([
        path('en/', include([
            path('', include('home.urls')),
            path('services/', include('services.urls')),
            path('news/', include('news.urls')),
            path('applications/', include('applications.urls')),
            path('debts/', include('debts.urls')),
            path('contacts/', include('contacts.urls')),
        ])),
    ])
    
    return urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
] + create_lang_urlpatterns()

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])
