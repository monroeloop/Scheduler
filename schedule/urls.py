"""schedule URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from pages import views as page_views
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views
from accounts.views import register, login, logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^pages/calendar_view/', page_views.calendar_view, name='calendar_view'),
    url(r'^pages/generate_day_html/', page_views.create_time_choice_html, name='generate_day_html'),
    url(r'^pages/appt_sub/', page_views.submitappt, name='appt_sub'),
    url(r'^$', page_views.main, name='main'),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', logout, name='logout'),
    url(r'^month/(?P<month>[-\d]{2})/(?P<year>[-\d]{4})$', page_views.month_view, name='month_view'),
    url(r'^accounts/appointment_submit/$', page_views.submitappt, name='appointment_submit'),
    url(r'^accounts/register/$', register, name='register'), # ^ means nothing can come before, while $ acts the same way as ^ except on the opposite end
]
