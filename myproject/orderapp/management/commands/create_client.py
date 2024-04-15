from django.core.management.base import BaseCommand

from ...models import Client


class Command(BaseCommand):
    help = "Create client."

    def handle(self, *args, **kwargs):
        client = Client(name='John',
                        email='john@example.com',
                        phone_number='9286054271',
                        address='Red Scwear,1')
        client.save()
        self.stdout.write(f'{client}')




