from django.core.management.base import BaseCommand, CommandError
from shortener.models import ShawtyURL

class Command(BaseCommand):
    help = 'Refresh all shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--num_items_refreshed', type=int)
        # '--' in front of argument denotes as optional argument
        # ex: ./manage.py refreshcodes --num_items_refreshed 10

    def handle(self, *args, **options):
        return ShawtyURL.objects.refresh_codes(items=options['num_items_refreshed'])