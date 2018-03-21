from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ('title', 'issue','reported_by','reported_on','priority','notes')
        # fields = ('title', 'issue','reported_by','reported_on','priority','assigned_to','status','resolution','verified','notes')

