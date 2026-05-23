from modeltranslation.translator import register, TranslationOptions
from .models import Service, ServiceCategory

@register(Service)
class ServiceTranslationOptions(TranslationOptions):
    fields = ('title', 'short_description', 'description')

@register(ServiceCategory)
class ServiceCategoryTranslationOptions(TranslationOptions):
    fields = ('title',)