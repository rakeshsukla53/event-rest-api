from django.core.management.base import BaseCommand
from eventbrite import Eventbrite
from keys import generic_keys

class Command(BaseCommand):
    help = "add all activities from event brite into database"

    def handle(self, *args, **options):
        eventbrite = Eventbrite(generic_keys.eventbrite_oauth_token)
        # washington_events = eventbrite.event_search(**{'venue.city': 'washington dc'})
        # print washington_events

        # passing parameters in url https://www.eventbriteapi.com/v3/events/search/?token=t&q=washington%20dc


