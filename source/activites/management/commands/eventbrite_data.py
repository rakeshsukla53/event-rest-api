from django.core.management.base import BaseCommand
from eventbrite import Eventbrite
from keys import generic_keys

class Command(BaseCommand):
    help = "add all activities from event brite into database"

    def handle(self, *args, **options):
        eventbrite = Eventbrite(generic_keys.eventbrite_oauth_token)

        # for getting all the events from washington DC
        # washington_events = eventbrite.event_search(**{'venue.city': 'washington dc'})
        # print washington_events

        # getting all the venue ID
        # print eventbrite.get('/venues/12847605')

        # getting all the ticket info
        # print eventbrite.get_event_ticket_classes(event_id=12882727585)
        # passing parameters in url https://www.eventbriteapi.com/v3/events/search/?token=t&q=washington%20dc


