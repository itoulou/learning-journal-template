from django.conf.urls import url
from software.views import view_languages, create_or_edit_language, delete_language, view_frameworks, create_or_edit_framework, \
                           delete_framework, view_databases, create_or_edit_database, delete_database, view_technologies,\
                           create_or_edit_technology, delete_technology


urlpatterns = [
    url(r'languages/$', view_languages, name="languages"),
    url(r'languages/(?P<pk>\d+)/edit/$', create_or_edit_language, name="update_language"),
    url(r'languages/new/$', create_or_edit_language, name="create_language"),
    url(r'languages/(?P<pk>\d+)/remove/$', delete_language, name="delete_language"),
    url(r'frameworks/$', view_frameworks, name="frameworks"),
    url(r'frameworks/(?P<pk>\d+)/edit/$', create_or_edit_framework, name="update_framework"),
    url(r'frameworks/new/$', create_or_edit_framework, name="create_framework"),
    url(r'frameworks/(?P<pk>\d+)/remove/$', delete_framework, name="delete_framework"),
    url(r'databases/$', view_databases, name="databases"),
    url(r'databases/(?P<pk>\d+)/edit/$', create_or_edit_database, name="update_database"),
    url(r'databases/new/$', create_or_edit_database, name="create_database"),
    url(r'databases/(?P<pk>\d+)/remove/$', delete_database, name="delete_database"),
    url(r'technologies/$', view_technologies, name="technologies"),
    url(r'technologies/(?P<pk>\d+)/edit/$', create_or_edit_technology, name="update_technology"),
    url(r'technologies/new/$', create_or_edit_technology, name="create_technology"),
    url(r'technologies/(?P<pk>\d+)/remove/$', delete_technology, name="delete_technology"),
]
