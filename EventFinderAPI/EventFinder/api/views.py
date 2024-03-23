from rest_framework.decorators import api_view
from EventFinder.models import Event
from EventFinder.api.serializers import EventSerializer
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime
from datetime import timedelta
from django.http import JsonResponse
import pandas as pd
import requests

@api_view(['POST'])
def getEventslist(request):
    user_inputs = request.data
    search_date = user_inputs.get('Date')
    start_date = datetime.strptime(search_date, '%Y-%m-%d')
    end_date  = start_date + timedelta(days=14)
    events_within_14_days = Event.objects.filter(date__range=(start_date, end_date)).values()
    
    event_list = list(events_within_14_days)
    event_list.sort(key=lambda x: x['date'])
    for i in range(len(event_list)):
        ls = event_list[i]
        weather_url = 'url'
        weather = requests.get(weather_url).json()
        
        distance_url = 'd_url'  
        distance = requests.get(distance_url).json()
        reslt = {
            "event_name": ls.get('event_name'), 
            "city_name": ls.get('city'), 
            "date": ls.get('date'), 
            "weather": weather['weather'], 
            "distance_km": distance['distance']
        }

        event_list[i] = reslt

    return Response(event_list)



@api_view(['POST'])
def EventAdd(request):
    serializer = EventSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)