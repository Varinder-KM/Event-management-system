from django.urls import path
from EventFinder.api.views import EventAdd, getEventslist
urlpatterns = [
    path('add/', EventAdd , name='Add-Events'),
    path('find/', getEventslist, name='Find-Events'),
]