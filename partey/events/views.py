from datetime import datetime, timedelta

from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from swingtime import models as swingtime

# Create your views here.
def home(request):
	events = swingtime.EventType.objects.all()	
	context = {
		'event_type': events,
	}
	return render(request, 'index.html', context)

def event_type(request, abbr):
	"""
		Function to load the events within 30 days from 
		the current date for specific categories.
	"""
	event_type = get_object_or_404(swingtime.EventType, abbr=abbr)
	now = timezone.now()
	occurrences = swingtime.Occurrence.objects.filter(
	    event__event_type=event_type,
	    start_time__gte=now,
	    start_time__lte=now+timedelta(days=+30)
	)
	context = {
		'occurrences': occurrences,
	    'event_type': event_type,
	}
	return render(request, 'swingtime/upcoming_by_event_type.html', context)