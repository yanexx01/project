from django.db import models


class News(models.Model):
    """Новость домофонной компании."""

    title = models.CharField(
        max_length=200,
        verbose_name='Заголовок'
    )
    slug = models.SlugField(
        max_length=200,
        unique=True,
        verbose_name='Слаг'
    )
    short_description = models.TextField(
        verbose_name='Краткое описание'
    )
    content = models.TextField(
        verbose_name='Содержимое'
    )
    image = models.ImageField(
        upload_to='news/',
        verbose_name='Изображение'
    )
    published_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата публикации'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-published_at']

    def __str__(self):
        return self.title
