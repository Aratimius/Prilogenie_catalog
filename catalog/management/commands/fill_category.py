from django.core.management import BaseCommand
from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'title': 'игры', 'description': 'большой ассортимент компьютерных игр по низким ценам!'},
            {'title': 'программы', 'description': 'полезные утилиты для вашего компьютера'}
        ]

        for category_item in category_list:
            Category.objects.create(**category_item)
