"""IssueTracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from accounts.views import index
from accounts import urls as accounts_urls
from packages import urls as urls_packages
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from packages.views import all_packages
from tickets import urls as urls_tickets
from charts import urls as urls_charts

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #url(r'^$', index, name="index"),
    url(r'^$', all_packages, name='index'),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^packages/', include(urls_packages)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^tickets/', include(urls_tickets)),
    url(r'^charts/', include(urls_charts)),
]
