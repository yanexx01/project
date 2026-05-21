from django.db import models
from django.utils.text import slugify


class ServiceCategory(models.Model):
    """Категория услуг домофонной компании."""

    title = models.CharField(
        max_length=200,
        verbose_name='Название категории'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Слаг'
    )

    class Meta:
        verbose_name = 'Категория услуг'
        verbose_name_plural = 'Категории услуг'
        ordering = ['title']

    def __str__(self):
        return self.title


class Service(models.Model):
    """Услуга домофонной компании."""

    category = models.ForeignKey(
        ServiceCategory,
        on_delete=models.CASCADE,
        related_name='services',
        verbose_name='Категория'
    )
    title = models.CharField(
        max_length=200,
        verbose_name='Название услуги'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Слаг'
    )
    short_description = models.TextField(
        verbose_name='Краткое описание'
    )
    description = models.TextField(
        verbose_name='Полное описание'
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Цена'
    )
    image = models.ImageField(
        upload_to='services/',
        verbose_name='Изображение'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
    )

    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуги'
        ordering = ['-created_at']

    def __str__(self):
        return self.title
