from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Команда для создания админки"""
    def handle(self, *args, **options):
        user = User.objects.create(
            email='admin@mail.ru',
            first_name='Artur',
            last_name='Belous',
            is_superuser=True,
            is_staff=True,
            is_active=True,
        )

        user.set_password('0204')
        user.save()
