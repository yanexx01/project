from django.db import models
from django.utils.translation import gettext_lazy as _


class Application(models.Model):
    """Заявка от клиента."""

    class ApplicationType(models.TextChoices):
        CONSULTATION = 'consultation', _('Консультация')
        SERVICE = 'service', _('Услуга')

    application_type = models.CharField(
        max_length=20,
        choices=ApplicationType.choices,
        default=ApplicationType.CONSULTATION,
        verbose_name='Тип заявки'
    )
    service = models.ForeignKey(
        'services.Service',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='applications',
        verbose_name='Услуга'
    )
    name = models.CharField(
        max_length=100,
        verbose_name='Имя'
    )
    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    message = models.TextField(
        verbose_name='Сообщение',
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Заявка'
        verbose_name_plural = 'Заявки'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.get_application_type_display()} - {self.name}'
