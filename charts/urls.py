from django.conf.urls import url, include
from .views import get_charts, get_data

urlpatterns = [
    url(r'^$', get_charts, name='get_charts'),
    url(r'^api/data/$', get_data, name='api-data'),
]