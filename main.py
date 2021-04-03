from __future__ import print_function
import datetime
import googleapiclient
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

calendarId = 'deniskin1992@gmail.com'
SERVICE_ACCOUNT_FILE = 'iconic-heading-309220-5791268ca5a0.json'


class GoogleCalendar(object):

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    # создание словаря с информацией о событии
    def create_event_dict(self):
        event = {
            'summary': 'Denis_test',
            'description': 'some info',
            'start': {
                'dateTime': '2021-03-31T20:30:00+03:00',
            },
            'end': {
                'dateTime': '2021-03-31T21:30:00+03:00',
            }
        }
        return event

    # создание события в календаре
    def create_event(self, event):
        e = self.service.events().insert(calendarId=calendarId,
                                         body=event).execute()
        print('Event created: %s' % (e.get('id')))

    # вывод списка из десяти предстоящих событий
    def get_events_list(self, date=None):
        now = datetime.datetime.utcnow().isoformat() + 'Z'
        print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId=calendarId,
                                                   timeMin=now,
                                                   maxResults=10, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        data = {}
        lst = []

        # for i in events:
        #     lst.append(i['summary'])
        #     data[now] = lst
        #     print(data)

        if not events:
            print('No upcoming events found.')

        for event in events:
            lst.append(event['summary'])
            start = event['start'].get('date')
            data[start] = lst

        print(data)




calendar = GoogleCalendar()
print("+ - create event\n? - print event list\n")
c = input()


if c == '+':
    event = calendar.create_event_dict()
    calendar.create_event(event)
elif c == '?':
    calendar.get_events_list()
else:
    pass