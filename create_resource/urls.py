from django.conf.urls import url
from create_resource.views import create_resource

urlpatterns = [
    url(r'^$', create_resource, name="create_resource")
]