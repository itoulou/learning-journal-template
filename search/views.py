# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib import messages
from create_resource.models import Resource


# Create your views here.
def search(request):
    if request.method == "GET":
        search = request.GET.get('search', False)
        resource = Resource.objects

        if resource.filter(name__icontains=search):
            all_resources = resource.filter(name__icontains=search).order_by("-created_date")

        elif resource.filter(link__icontains=search):
            all_resources = resource.filter(link__icontains=search).order_by("-created_date")

        elif resource.filter(language__language__icontains=search):
            all_resources = resource.filter(language__language__icontains=search).order_by("-created_date")

        elif resource.filter(framework__framework__icontains=search):
            all_resources = resource.filter(framework__framework__icontains=search).order_by("-created_date")

        elif resource.filter(database__database__icontains=search):
            all_resources = resource.filter(database__icontains=search).order_by("-created_date")

        elif resource.filter(technology__technology__icontains=search):
            all_resources = resource.filter(technology__technology__icontains=search).order_by("-created_date")

        else:
            all_resources = None
            messages.error(request, "No results found")

        return render(request, 'index.html', {"all_resources": all_resources})


def search_software(request, software):

    translation_table = dict.fromkeys(map(ord, '-'), ' ')
    software = software.title().translate(translation_table)

    resource = Resource.objects

    if resource.filter(language__language__icontains=software):
        all_resources = resource.filter(language__language__icontains=software).order_by("-created_date")

    elif resource.filter(framework__framework__icontains=software):
        all_resources = resource.filter(framework__framework__icontains=software).order_by("-created_date")

    elif resource.filter(database__database__icontains=software):
        all_resources = resource.filter(database__database__icontains=software).order_by("-created_date")

    elif resource.filter(technology__technology__icontains=software):
        all_resources = resource.filter(technology__technology__icontains=software).order_by("-created_date")

    else:
        all_resources = None
        messages.error(request, "No results found")

    return render(request, 'index.html', {"all_resources": all_resources})
