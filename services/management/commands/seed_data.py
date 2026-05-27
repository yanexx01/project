from django.core.management.base import BaseCommand
from services.models import ServiceCategory, Service
from news.models import News
from contacts.models import ContactInfo
from django.utils.text import slugify
from django.core.files.base import ContentFile
from decimal import Decimal
from PIL import Image, ImageDraw, ImageFont
import io


class Command(BaseCommand):
    help = 'Заполняет БД начальными данными'

    def handle(self, *args, **options):
        self.stdout.write('🌱 Начинаю заполнение БД...\n')

        # Очистка (опционально, раскомментируй если нужно)
        # ServiceCategory.objects.all().delete()
        # Service.objects.all().delete()
        # News.objects.all().delete()

        # Создание категорий услуг
        categories_data = [
            {'title': 'Установка', 'slug': 'ustanovka'},
            {'title': 'Обслуживание', 'slug': 'obsluzhivanie'},
            {'title': 'Ремонт', 'slug': 'remont'},
            {'title': 'Модернизация', 'slug': 'modernizacija'},
        ]

        categories = {}
        for cat_data in categories_data:
            cat, created = ServiceCategory.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={'title': cat_data['title']}
            )
            categories[cat_data['slug']] = cat
            status = '✓ Создана' if created else '~ Уже существует'
            self.stdout.write(f"  {status}: {cat.title}")

        self.stdout.write('\n📋 Категории услуг добавлены\n')

        # Создание услуг
        services_data = [
            {
                'title': 'Установка домофона',
                'slug': 'ustanovka-domofona',
                'short_description': 'Профессиональная установка современных домофонных систем',
                'description': 'Мы выполняем полный спектр работ по установке домофонов от выбора оборудования до его монтажа и настройки.',
                'category_slug': 'ustanovka',
                'price': Decimal('15000.00'),
                'price_unit': 'руб./система',
            },
            {
                'title': 'Техническое обслуживание',
                'slug': 'tehnicheskoe-obsluzhivanie',
                'short_description': 'Регулярное техническое обслуживание и проверка систем',
                'description': 'Профилактическое обслуживание домофонных систем для их надежной работы.',
                'category_slug': 'obsluzhivanie',
                'price': Decimal('5000.00'),
                'price_unit': 'руб./месяц',
            },
            {
                'title': 'Экстренный ремонт',
                'slug': 'ekstrenniy-remont',
                'short_description': 'Срочный ремонт неработающих систем 24/7',
                'description': 'Мы предоставляем услугу экстренного ремонта в любое время дня и ночи.',
                'category_slug': 'remont',
                'price': Decimal('8000.00'),
                'price_unit': 'руб./выезд',
            },
            {
                'title': 'Модернизация системы',
                'slug': 'modernizacija-sistemy',
                'short_description': 'Обновление и улучшение существующих домофонных систем',
                'description': 'Замена устаревшего оборудования на современное с сохранением существующих линий.',
                'category_slug': 'modernizacija',
                'price': Decimal('25000.00'),
                'price_unit': 'руб./система',
            },
        ]

        for svc_data in services_data:
            category = categories[svc_data.pop('category_slug')]
            svc, created = Service.objects.get_or_create(
                slug=svc_data['slug'],
                defaults={
                    **svc_data,
                    'category': category,
                }
            )
            status = '✓ Создана' if created else '~ Уже существует'
            self.stdout.write(f"  {status}: {svc.title}")

        self.stdout.write('\n✅ Услуги добавлены\n')

        # Создание новостей
        news_data = [
            {
                'title': 'Запущена новая версия мобильного приложения',
                'slug': 'novoe-mobilnoe-prilozhenie',
                'short_description': 'Мы запустили улучшенную версию приложения для управления домофоном',
                'content': 'Новая версия включает поддержку видеозвонков и улучшенный интерфейс.',
            },
            {
                'title': 'Расширение сервисного центра',
                'slug': 'rasshirenie-servisa',
                'short_description': 'Открыт новый сервисный центр в центре города',
                'content': 'Новый центр позволит нам быстрее обслуживать клиентов в центральной части города.',
            },
            {
                'title': 'Скидки на услуги обслуживания',
                'slug': 'skidki-na-obsluzhivanie',
                'short_description': 'До конца месяца действует скидка 15% на годовое обслуживание',
                'content': 'Скидка распространяется на все виды систем домофонов.',
            },
        ]

        for news_data_item in news_data:
            news, created = News.objects.get_or_create(
                slug=news_data_item['slug'],
                defaults=news_data_item
            )
            status = '✓ Создана' if created else '~ Уже существует'
            self.stdout.write(f"  {status}: {news.title}")

        self.stdout.write('\n📰 Новости добавлены\n')

        # Создание контактов
        contact, created = ContactInfo.objects.get_or_create(
            defaults={
                'phone': '+7 (978) 123-45-67',
                'email': 'info@intercom.ru',
                'address': 'п-ов Крым, г. Евпатория',
                'telegram': 'https://t.me/intercom_company',
                'whatsapp': 'https://wa.me/79781234567',
            }
        )
        status = '✓ Создан' if created else '~ Уже существует'
        self.stdout.write(f"  {status}: Контакты\n")

        self.stdout.write(
            self.style.SUCCESS('✅ БД успешно заполнена начальными данными!')
        )
