from django.db import models


class Debt(models.Model):
    """Задолженность клиента."""

    account_number = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='Номер лицевого счёта'
    )
    full_name = models.CharField(
        max_length=200,
        verbose_name='ФИО'
    )
    amount = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Сумма задолженности'
    )
    is_paid = models.BooleanField(
        default=False,
        verbose_name='Оплачено'
    )

    class Meta:
        verbose_name = 'Задолженность'
        verbose_name_plural = 'Задолженности'
        ordering = ['-is_paid', 'account_number']

    def __str__(self):
        return f'{self.account_number} - {self.full_name}'
