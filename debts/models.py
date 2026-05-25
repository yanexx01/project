from django.db import models


class Debt(models.Model):
    """Задолженность клиента."""

    account_number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Номер лицевого счёта'
    )
    last_name = models.CharField(
        max_length=100,
        verbose_name='Фамилия'
    )
    address = models.CharField(
        max_length=200,
        verbose_name='Адрес'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма задолженности'
    )
    last_updated = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата обновления'
    )

    class Meta:
        verbose_name = 'Задолженность'
        verbose_name_plural = 'Задолженности'
        ordering = ['-last_updated', 'account_number']

    def __str__(self):
        return f'{self.account_number} - {self.last_name}'
