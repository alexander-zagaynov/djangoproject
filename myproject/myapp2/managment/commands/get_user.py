from django.core.management.base import BaseCommand
from myproject.myapp2.models import User


class Command(BaseCommand):
    help = "Get user by id."

    def add_arguments(self, parser):
        parser.add_argument('pk', type=int, help='User ID')

    def handle(self, *args, **kwargs):
        pk = kwargs['pk']
        user = User.objects.get(pk=pk)
        self.stdout.write(f'{user}')

