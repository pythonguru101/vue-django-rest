from django.core.management.base import BaseCommand

from server.api.fixtures.factories import (
    UserFactory,
    ShopFactory,
)


class Command(BaseCommand):
    def handle(self, *args, **options):
        UserFactory()
        UserFactory()
        UserFactory()
        UserFactory()
        UserFactory()

        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
        ShopFactory()
