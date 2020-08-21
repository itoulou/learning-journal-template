from django.conf.urls import url

from search.views import search, search_software

urlpatterns = [
    url(r'^$', search, name='search'),
    url(r'^(?P<software>[-\w\d]+)/$', search_software, name='search_software')
]