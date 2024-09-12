import json
from catalog.models import Product, Category
from django.core.management import BaseCommand


class Command(BaseCommand):
    """Наполняем БД данными из data.json"""
    @staticmethod
    def json_read_data():
        with open("data.json") as json_file:
            data = json.load(json_file)
        return data

    def handle(self, *args, **options):
        Product.objects.all().delete
        Category.objects.all().delete

        products_for_create = []
        categories_for_create = []

        for item in Command.json_read_data():
            if item["model"] == "catalog.category":
                categories_for_create.append(
                    Category(
                        pk=item["pk"],
                        title=item["fields"]["title"],
                        description=item["fields"]["description"],
                    )
                )
        Category.objects.bulk_create(categories_for_create)

        for item in Command.json_read_data():
            if item["model"] == "catalog.product":
                products_for_create.append(
                    Product(
                        pk=item["pk"],
                        title=item["fields"]["title"],
                        description=item["fields"]["description"],
                        image=item["fields"]["image"],
                        category=Category.objects.get(pk=item["fields"]["category"]),
                        price=item["fields"]["price"],
                        creation_date=item["fields"]["creation_date"],
                        last_mod_date=item["fields"]["last_mod_date"],
                    )
                )
        Product.objects.bulk_create(products_for_create)

# Столько мороки, чтобы получить тот же loaddata data.json...
