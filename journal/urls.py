"""journal URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from journal_resource.views import home, delete_resource, update_resource
from create_resource import urls as create_resource_urls
from search import urls as search_urls
from software import urls as software_urls

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$', home, name='home'),
    url(r'^update_resource/(?P<pk>\d+)/$', update_resource, name="update_resource"),
    url(r'^delete_resource/(?P<pk>\d+)/$', delete_resource, name="delete_resource"),
    url(r'^create-resource/', include(create_resource_urls)),
    url(r'^search/', include(search_urls)),
    url(r'^software/', include(software_urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
