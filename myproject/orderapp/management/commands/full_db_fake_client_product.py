from django.core.management.base import BaseCommand

from ...models import Client, Product, Order


class Command(BaseCommand):
    help = "Generate fake Client,Product and Order."

    def add_arguments(self, parser):
        parser.add_argument('count', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        count = kwargs.get('count')
        for i in range(1, count + 1):
            client = Client(name=f'John{i}',
                            email=f'john_{i}@example.com',
                            phone_number=f'928605427{i}',
                            address=f'Red Scwear,{i}')

            client.save()
        for i in range(1, count + 1):
            product = Product(name=f'product{i}',
                              description=f'description{i}',
                              price=10 + i,
                              quantity=i)
            product.save()

            order = Order(client=f'John{i}',
                          #products=product.name(f'product{i}'),
                          total_amount=i)

            order.save()
