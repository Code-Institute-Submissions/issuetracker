from django.conf.urls import url, include
from .views import get_tickets, ticket_detail, create_or_edit

urlpatterns = [
    url(r'^$', get_tickets, name='get_tickets'),
    url(r'^(?P<pk>\d+)/$', ticket_detail, name='ticket_detail'),
    url(r'^new/$', create_or_edit, name='create_ticket'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_edit, name='edit_ticket'),
]