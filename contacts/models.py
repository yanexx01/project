from django.db import models


class ContactInfo(models.Model):
    """Контактная информация компании."""

    phone = models.CharField(
        max_length=20,
        verbose_name='Телефон'
    )
    email = models.EmailField(
        verbose_name='Email'
    )
    address = models.CharField(
        max_length=300,
        verbose_name='Адрес'
    )
    telegram = models.URLField(
        blank=True,
        verbose_name='Telegram'
    )
    whatsapp = models.URLField(
        blank=True,
        verbose_name='WhatsApp'
    )

    class Meta:
        verbose_name = 'Контактная информация'
        verbose_name_plural = 'Контактная информация'

    def __str__(self):
        return f'{self.phone} - {self.email}'
