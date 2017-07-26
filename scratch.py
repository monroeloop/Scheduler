import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'schedule.settings')

import django

django.setup()
from pages.models import Appointment
import datetime


def check_if_in_timerange(check_time, range_start, range_end):
    return range_start <= check_time <= range_end


fmt = '%Y-%m-%d %H:%M:%S'
day_start = '2017-07-18 09:00:00'
day_end = '2017-07-18 15:45:00'
start = datetime.datetime.strptime(day_start, fmt)
end = datetime.datetime.strptime(day_end, fmt)

start_html = datetime.datetime.strptime(day_start, fmt)
end_html = datetime.datetime.strptime(day_end, fmt)
appts = Appointment.objects.all().order_by('start')
html = ''
day = []

while start < end:
    day.append(start)
    start += datetime.timedelta(minutes=15)


for time in day:
    has_appt = False
    for apt in appts:
        if check_if_in_timerange(time, apt.start, apt.end):
            has_appt = True
            break
    if has_appt:
        html += '<div id="rowthree" class="rowthree booked" data-time="{}" title="Select Times"></div>'.format(time.strftime('%H:%M'))
    else:
        html += '<div id="rowthree" class="rowthree" data-time="{}" title="Select Times"></div>'.format(time.strftime('%H:%M'))

# print(day)
print(html)

