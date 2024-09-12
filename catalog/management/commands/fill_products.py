from django.core.management import BaseCommand
from catalog.models import Product, Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        product_list = [
            {
                "title": "Dead space",
                "description": "компьютерная игра в жанре survival horror, разработанная Motive Studio и изданная Electronic Arts. Ремейк одноимённой игры 2008 года, разработанной EA Redwood Shores.",
                "category": Category.objects.get(title='игры'),
                "price": 4000
            },
            {
                "title": "God of war",
                "description": "компьютерная игра в жанре action-adventure, разработанная компанией SIE Santa Monica Studio и изданная Sony Interactive Entertainment для игровой консоли PlayStation 4, а затем на Windows.",
                "category": Category.objects.get(title='игры'),
                "price": 6000,
            },
            {
                "title": "Cyberpunk 2077",
                "description": "компьютерная игра в жанре Action/RPG в открытом мире, разработанная и изданная польской студией CD Projekt",
                "category": Category.objects.get(title='игры'),
                "price": 4000,
            },
            {
                "title": "NordVPN",
                "description": "надежный VPN",
                "category": Category.objects.get(title='программы'),
                "price": 1000,
            }
        ]

        for product_item in product_list:
            Product.objects.create(**product_item)
