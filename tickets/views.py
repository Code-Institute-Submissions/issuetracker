from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Ticket
from .forms import TicketForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


@login_required
def get_tickets(request):
    """
    Create a view that will return a list
    of tickets that were entered and render
    them to the 'request_ticket.html'
    """
    
    tickets = Ticket.objects.filter(reported_on__lte=timezone.now()).order_by('-reported_on')
    return render(request, "request_ticket.html", {'tickets':tickets})
    
@login_required
def ticket_detail(request, pk):
    """
    Create a view that returns a single
    ticket object based on the ticket id (pk)
    and render it to the 'ticket_detail.html' template
    or return a 404 error if the ticket is not found
    """
    
    ticket = get_object_or_404(Ticket, pk=pk)
    ticket.views += 1
    ticket.save()
    return render(request, "ticket_detail.html",{'ticket':ticket})

@login_required
def create_or_edit(request, pk=None):
    """
    Create a view that allows us to create 
    or edit a ticket depending if the Ticket 
    ID is null or not
    """
    
    ticket = get_object_or_404(Ticket, pk=pk) if pk else None
    if request.method == "POST":
        form = TicketForm(request.POST, instance=ticket)
        if form.is_valid():
            user=User.objects.get(email=request.user.email)
            
            ticket = form.save()
            ticket.profile_user=user.email
            ticket.save()
            return redirect(ticket_detail, ticket.pk)
    else:
        form = TicketForm(instance=ticket)
    return render(request, 'ticketform.html', {'form':form})