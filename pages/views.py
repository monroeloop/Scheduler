import datetime
from calendar import *
from django.shortcuts import render, HttpResponseRedirect
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from datetime import date
from django.views.decorators.csrf import csrf_exempt

from .models import Appointment


# Create your views here.
def check_if_in_timerange(check_time, range_start, range_end):
    return range_start <= check_time <= range_end


@csrf_exempt
def create_time_choice_html(request):
        if request.method == 'POST':
            year = request.POST.get('year')
            month = request.POST.get('month')
            day = request.POST.get('day')
            fmt = '%Y-%m-%d %H:%M:%S'
            day_start = '{}-{}-{} 09:00:00'.format(year, int(month) - 1, day)
            day_end = '{}-{}-{} 15:45:00'.format(year, int(month) - 1, day)
            start = datetime.datetime.strptime(day_start, fmt)
            end = datetime.datetime.strptime(day_end, fmt)
            print(start)
            print(end)
            date = datetime.datetime(int(year), int(month), int(day))
            appts = Appointment.objects.filter(start__day=date.day).order_by('start')
            print(appts)
            html = []
            day = []

            while start <= end:
                day.append(start)
                start += datetime.timedelta(minutes=15)

            for time in day:
                has_appt = False
                for apt in appts:
                    if check_if_in_timerange(time, apt.start, apt.end):
                        has_appt = True
                        break
                if has_appt:
                    html.append("<div id='rowthree-booked' class='rowthree booked' data-time='{}' title='Select Times'></div>".format(
                        time.strftime('%H:%M')))
                else:
                    html.append("<div id='rowthree' class='rowthree' data-time='{}' title='Select Times'></div>".format(
                        time.strftime('%H:%M')))
            return JsonResponse({'html': html})


class SchedulingCalendar(HTMLCalendar):
    def __init__(self):
        super(SchedulingCalendar, self).__init__()
        self.today = datetime.date.today()

    def get_week(self, date):
        one_day = datetime.timedelta(days=1)
        day_idx = (date.weekday()) % 7  # turn sunday into 0, monday into 1, etc.
        sunday = date - datetime.timedelta(days=day_idx)
        date = sunday

        for n in range(7):
            yield date
            date += one_day


def calendar_view(request):
    timeslots = range(29)
    minutes = ["00", "15", "30", "45"]
    hours = ["9", "10", "11", "12", "1", "2", "3"]
    # for h in hours:
    #     for m in minutes:
    #         print('{}{}'.format(h, m))

    then = datetime.datetime(2000, 1, 1, 9, 00)
    end = then + datetime.timedelta(hours=6)
    l = []
    while then <= end:
        l.append(then)
        then += datetime.timedelta(minutes=60)
    times = [t.strftime("%I %p") for t in l]

    events = []

    now = datetime.datetime.now()
    calendar = HTMLCalendar().formatmonth(now.year, now.month)

    return render(request, 'pages/calendar_view.html',
                  {"year": datetime.datetime.today().year, "month": datetime.datetime.today(), "h": hours, "m": minutes,
                   "timeslots": timeslots, "times": times, "calendar": calendar})


def month_view(request, month, year):
    cal = calendar.formatmonth(int(year), int(month))
    date = datetime.date(int(year), int(month), 1)
    next_month = int(month) + 1 if int(month) + 1 <= 12 else 1
    prev_month = int(month) - 1 if int(month) - 1 >= 1 else 12
    month_nav = {
        'next': {'year': int(year) + 1,
                 'month': str(next_month) if len(str(next_month)) > 1 else '0' + str(next_month)},
        'prev': {'year': int(year) - 1,
                 'month': str(prev_month) if len(str(prev_month)) > 1 else '0' + str(prev_month)},
        'this_year': datetime.date.today().year,
        'this_month': datetime.date.today().month if len(str(datetime.date.today().month)) > 1 else '0' + str(
            datetime.date.today().month),
    }
    return render(request, 'pages/month.html', {'cal': cal, 'dt': date, 'cal_nav': month_nav})


def main(request):
    return render(request, 'pages/main.html', {})


def submitappt(request):
    if request.method == "POST":
        for k, v in request.POST.items():
            print("key: {}, value: {}".format(k, v))

        appointments = Appointment()
        appointments.start = request.POST.get('start')
        appointments.end = request.POST.get('end')
        appointments.title = request.POST.get('title')
        appointments.note = request.POST.get('note')
        appointments.save()
        #
        # start_conflict = Appointment.objects.filter(
        #     start_time__range=(appointments.start_time,
        #                        appointments.end_time))
        # end_conflict = Appointment.objects.filter(
        #     end_time__range=(appointments.start_time,
        #                      appointments.end_time))
        #
        # during_conflict = Appointment.objects.filter(
        #     start_date__lte=appointments.start_time,
        #     end_date__gte=appointments.end_time)
        #
        # if (start_conflict or end_conflict or during_conflict):
        #     pass

        return HttpResponseRedirect("/pages/calendar_view/")




        #    def formatday(self, day, weekday, theyear, themonth):
        #        """
        #        Return a day as a table cell.
        #        """
        #        id = ''
        #        appointments = []
        #        if day !=0:
        #            appointments = Appointments.objects.filter(date = datetime.date(theyear, themonth, day))
        #
        #            if self.today == datetime.date(theyear, themonth, day):
        #                id = 'Today'
        #            else:
        #                id = 'dt_{}'.format(day)
        #
        #        if day == 0:
        #            return '<div class="noday">&nbsp;</div>'  # day outside month
        #        elif len(appointments) > 0:
        #            html = '<div id="{id}" class="{day}" data-day="{day}" data-month="{month}" data-year="{year}">' \
        #                   '<div class="dayHolder">{day}</div>'.format(id=id, day=day, month=themonth, year=theyear)
        #            for i in appointments:
        #                html += '<div class="task item"><a href="{}"></a></div>'.format(i.title)
        #            html += '</div>'
        #            return html
        #        else:
        #            return '<div id="{id}" class="{day}" data-day="{day}" data-month="{month}" data-year="{year}"><div class="dayHolder">{day}</div></div>'.format(
        #
        #                id=id, day=day, month=themonth, year=theyear)
        #
        #
        #        def formatweek(self, theweek, theyear, themonth):
        #
        #            """
        #            Return a complete week as a table row.
        #            """
        #
        #            s = ''.join(self.formatday(d, wd, theyear, themonth) for (d, wd) in theweek)
        #            return '<div class="week">%s</div>' % s
        #
        #        def formatweekday(self, day):
        #
        #            """
        #            Return a weekday name as a table header.
        #            """
        #
        #            return '<div class="%s day">%s</div>' % (self.cssclasses[day], day_abbr[day])
        #
        #        def formatweekheader(self):
        #
        #            """
        #            Return a header for a week as a table row.
        #            """
        #
        #            s = ''.join(self.formatweekday(i) for i in self.iterweekdays())
        #
        #            return '<div class="weekHeader">%s</div>' % s
        #
        #        def formatmonthname(self, theyear, themonth, withyear=True):
        #
        #            """
        #            Return a month name as a table row.
        #            """
        #
        #            if withyear:
        #                s = '{} {}'.format(month_name[themonth], theyear)
        #
        #            else:
        #                s = '%s' % month_name[themonth]
        #
        #            return '<div><div class="monthTitle"><h4>%s</h4></div></div>' % s
        #
        #        def formatmonth(self, theyear, themonth, withyear=True):
        #
        #            """
        #
        #            Return a formatted month as a table.
        #
        #            """
        #
        #            v = []
        #
        #            a = v.append
        #
        #            a('<div class="month">')
        #
        #            a('\n')
        #
        #            a(self.formatmonthname(theyear, themonth, withyear=withyear))
        #
        #            a('\n')
        #
        #            a(self.formatweekheader())
        #
        #            a('\n')
        #
        #            for week in self.monthdays2calendar(theyear, themonth):
        #                a(self.formatweek(week, theyear, themonth))
        #
        #                a('\n')
        #
        #            a('</div>')
        #
        #            a('\n')
        #
        #            return ''.join(v)
        #
        #        def get_week(self, date):
        #
        #            """Return the full week (Sunday first) of the week containing the given date.
        #
        #
        #
        #            'date' may be a datetime or date instance (the same type is returned).
        #
        #            """
        #
        #            one_day = datetime.timedelta(days=1)
        #
        #            day_idx = (date.weekday()) % 7  # turn sunday into 0, monday into 1, etc.
        #
        #            sunday = date - datetime.timedelta(days=day_idx)
        #
        #            date = sunday
        #
        #            for n in range(7):
        #                yield date
        #
        #                date += one_day
        #
        #        def week_html(self):
        #
        #            """Return HTML for the week"""
        #
        #            week_days = list(self.get_week(datetime.datetime.now().date()))
        #
        #            html = '<div class="weekContainer">' \
        # \
        #                   '<div class="weekTitle"><h4>Week of {} - {}</h4></div>'.format(week_days[0].strftime("%b %d"),
        #
        #                                                                                  week_days[-1].strftime("%b - %d"))
        #
        #        for day in week_days:
        #
        #            tasks = Tasks.objects.filter(date=day)
        #
        #            css = 'weekDay'
        #
        #            if day.strftime("%a").lower() == 'sun' or day.strftime("%a").lower() == 'sat' or self.is_holiday(day):
        #                css += ' holiday'
        #
        #            html += '<div class="{cls}"><div class="dateHolder">{date}</div>'.format(cls=css,
        #
        #                                                                                     date=day.strftime("%b - %d"))
        #
        #            if len(tasks) > 0:
        #
        #                for i in tasks:
        #                    html += '<div class="task"><a href="{}">{}</a></div>'.format(i.link, i.title)
        #
        #            html += '</div>'
        #
        #        html += '</div>'
        #
        #        return html
        #
        #    def formatweek(self, theweek):
        #        """
        #        Return a complete week as a table row.
        #        """
        #        s = ''.join(self.formatday(d, wd) for (d, wd) in theweek)
        #        return '<ul>%s</ul>' % s
        #
        #
