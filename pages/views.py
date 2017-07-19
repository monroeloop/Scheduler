import datetime
from calendar import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date

from .models import Appointments




# Create your views here.

def calendar_view(request):
    # timeslots = range(32)
    then = datetime.datetime(2000, 1, 1, 9, 00)
    end = then+datetime.timedelta(hours=6)
    l = []
    while then <= end:
        l.append(then)
        then += datetime.timedelta(minutes=15)
    times = [t.strftime("%I:%M %p") for t in l]

    now = datetime.datetime.now()
    calendar = HTMLCalendar().formatmonth(now.year, now.month)
    # calendar = SchedulingCalendar
    return render(request, 'pages/calendar_view.html', {"times": times, "calendar": calendar})

def main(request):
    return render(request, 'pages/main.html', {})

class SchedulingCalendar(HTMLCalendar):
    def __init__(self):
        self.today = datetime.date.today()

    def formatday(self, day, weekday, theyear, themonth):
        """
        Return a day as a table cell.
        """
        id = ''
        appointments = []
        if day !=0:
            appointments = Appointments.objects.filter(date = datetime.date(theyear, themonth, day))

            if self.today == datetime.date(theyear, themonth, day):
                id = 'Today'
            else:
                id = 'dt_{}'.format(day)

        if day == 0:
            return '<div class="noday">&nbsp;</div>'  # day outside month
        elif len(appointments) > 0:
            html = '<div id="{id}" class="{day}" data-day="{day}" data-month="{month}" data-year="{year}">' \
                   '<div class="dayHolder">{day}</div>'.format(id=id, day=day, month=themonth, year=theyear)
            for i in appointments:
                html += '<div class="task item"><a href="{}"></a></div>'.format(i.title)
            html += '</div>'
            return html
        else:
            return '<div id="{id}" class="{day}" data-day="{day}" data-month="{month}" data-year="{year}"><div class="dayHolder">{day}</div></div>'.format(

                id=id, day=day, month=themonth, year=theyear)


        def formatweek(self, theweek, theyear, themonth):

            """
            Return a complete week as a table row.
            """

            s = ''.join(self.formatday(d, wd, theyear, themonth) for (d, wd) in theweek)
            return '<div class="week">%s</div>' % s

        def formatweekday(self, day):

            """
            Return a weekday name as a table header.
            """

            return '<div class="%s day">%s</div>' % (self.cssclasses[day], day_abbr[day])

        def formatweekheader(self):

            """
            Return a header for a week as a table row.
            """

            s = ''.join(self.formatweekday(i) for i in self.iterweekdays())

            return '<div class="weekHeader">%s</div>' % s

        def formatmonthname(self, theyear, themonth, withyear=True):

            """
            Return a month name as a table row.
            """

            if withyear:
                s = '{} {}'.format(month_name[themonth], theyear)

            else:
                s = '%s' % month_name[themonth]

            return '<div><div class="monthTitle"><h4>%s</h4></div></div>' % s

        def formatmonth(self, theyear, themonth, withyear=True):

            """

            Return a formatted month as a table.

            """

            v = []

            a = v.append

            a('<div class="month">')

            a('\n')

            a(self.formatmonthname(theyear, themonth, withyear=withyear))

            a('\n')

            a(self.formatweekheader())

            a('\n')

            for week in self.monthdays2calendar(theyear, themonth):
                a(self.formatweek(week, theyear, themonth))

                a('\n')

            a('</div>')

            a('\n')

            return ''.join(v)

        def get_week(self, date):

            """Return the full week (Sunday first) of the week containing the given date.



            'date' may be a datetime or date instance (the same type is returned).

            """

            one_day = datetime.timedelta(days=1)

            day_idx = (date.weekday()) % 7  # turn sunday into 0, monday into 1, etc.

            sunday = date - datetime.timedelta(days=day_idx)

            date = sunday

            for n in range(7):
                yield date

                date += one_day

        def week_html(self):

            """Return HTML for the week"""

            week_days = list(self.get_week(datetime.datetime.now().date()))

            html = '<div class="weekContainer">' \
 \
                   '<div class="weekTitle"><h4>Week of {} - {}</h4></div>'.format(week_days[0].strftime("%b %d"),

                                                                                  week_days[-1].strftime("%b - %d"))

        for day in week_days:

            tasks = Tasks.objects.filter(date=day)

            css = 'weekDay'

            if day.strftime("%a").lower() == 'sun' or day.strftime("%a").lower() == 'sat' or self.is_holiday(day):
                css += ' holiday'

            html += '<div class="{cls}"><div class="dateHolder">{date}</div>'.format(cls=css,

                                                                                     date=day.strftime("%b - %d"))

            if len(tasks) > 0:

                for i in tasks:
                    html += '<div class="task"><a href="{}">{}</a></div>'.format(i.link, i.title)

            html += '</div>'

        html += '</div>'

        return html

    def formatweek(self, theweek):
        """
        Return a complete week as a table row.
        """
        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        return '<ul>%s</ul>' % s


