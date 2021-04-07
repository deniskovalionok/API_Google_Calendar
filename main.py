from __future__ import print_function
import datetime
import googleapiclient
from google.oauth2 import service_account
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/calendar']

calendarId = 'deniskin1992@gmail.com'
SERVICE_ACCOUNT_FILE = 'iconic-heading-309220-5791268ca5a0.json'

time = ''


class GoogleCalendar(object):

    def __init__(self):
        credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = googleapiclient.discovery.build('calendar', 'v3', credentials=credentials)

    def get_events_list(self):

        data = {}
        now1 = ''
        i = 0
        now = datetime.datetime.utcnow().isoformat() + 'Z'

        for e in now:
            i = i + 1
            now1 = now1 + e
            if (i == 12):
                break
            timeMin = now1 + "05:00:00+03:00"
            timeMax = now1 + "22:00:00+03:00"

        print(now1)
        events_result = self.service.events().list(calendarId=calendarId,
                                                   timeMin=timeMin,
                                                   timeMax=timeMax, singleEvents=True,
                                                   orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        i = 1
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            time = start[11] +start[12] + start[13] + start[14] + start[15]
            data[time] = event['summary']


        print(data)


calendar = GoogleCalendar()
calendar.get_events_list()
