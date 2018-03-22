from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from tickets.models import Ticket
from django.core import serializers
from django.http import HttpResponse



@login_required
def get_charts(request):
    """
    Create a view that will return a chart
    and render
    them to the 'request_chart.html'
    """
    
    return render(request, "request_chart.html")

@login_required
def get_data(request):
    """
    Sending all ticket in json format to api/data/
    """
    x='reported_by'
    
    ticket = Ticket.objects.all()
    
    return HttpResponse(serializers.serialize('json', list(ticket)), content_type="application/json")
    #return render(request, "request_chart.html")