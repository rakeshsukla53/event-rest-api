from django.core.management.base import BaseCommand
from eventbrite import Eventbrite
from keys import generic_keys
from activites.models import Activity
# from ...models import Activity it will also work


class Command(BaseCommand):
    help = "add all activities from event brite into database"

    def handle(self, *args, **options):
        eventbrite = Eventbrite(generic_keys.eventbrite_oauth_token)
        # for getting all the events from washington DC
        # **{'venue.city': 'new york'}
        nyc_events = []
        for i in range(2, 500):
            try:
                nyc_events = eventbrite.event_search(**{'page': i})['events']
            except:
                pass
            for line in nyc_events:
                event_name, event_description, event_website, event_image, start_date, start_time, end_date, end_time, event_address, event_faq, phone_number = '', '', '', '', '', '', '', '', '', '', ''
                try:
                    event_name = line['name']['text']
                    event_description = line['description']['text']
                except:
                    pass
                try:
                    event_website = line['url']
                    event_image = line['logo']['url']
                except:
                    pass
                try:
                    start_time = line['start']['local'].split('T')[1]
                    start_date = line['start']['local'].split('T')[0]
                    end_time = line['end']['local'].split('T')[1]
                    end_date = line['end']['local'].split('T')[0]
                except:
                    pass
                try:
                    event_address = eventbrite.get('/venues/{}/'.format(line['venue_id']))['address']['address_1']
                except Exception as e:
                    print e

                try:
                    Activity.objects.create(event_name=event_name, event_location=event_address, event_address=event_address, event_website=event_website, event_description=event_description, event_image=event_image, start_time=start_time, end_time=end_time, start_date=start_date, end_date=end_date, event_faq=event_faq)
                except Exception as e:
                    print e

            # getting all the ticket info
            # print eventbrite.get_event_ticket_classes(event_id=12882727585)
            # passing parameters in url https://www.eventbriteapi.com/v3/events/search/?token=t&q=washington%20dc

