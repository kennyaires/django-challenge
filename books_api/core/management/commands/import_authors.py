from django.core.management.base import BaseCommand
import csv

from core.models import Author


class Command(BaseCommand):
    """Django command to seed author database with csv data"""

    def add_arguments(self, parser):
        parser.add_argument('file', type=str)

    def handle(self, *args, **options):
        """Handle the command"""
        source_file = options['file']
        self.stdout.write(f'Checking if {source_file} exists...')

        try:
            # Open csv and loads info to db
            with open(source_file, 'r') as file:

                rows = list(csv.reader(file))
                count = 0

                for idx in range(1, len(rows)):
                    author = Author.objects.filter(name=rows[idx][0]).first()
                    if not author:
                        author = Author(name=rows[idx][0])
                        author.save()
                        count += 1

                self.stdout.write(self.style.SUCCESS(
                    f'Authors table populated with {count} authors!'
                    ))

        except FileNotFoundError:
            self.stdout.write(self.style.ERROR('File not found!'))
