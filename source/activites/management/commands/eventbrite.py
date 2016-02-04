from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "add all activities from event brite into database"

    def handle(self, *args, **options):
        print "python script is running online"
