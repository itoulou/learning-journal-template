# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from create_resource.models import Resource
from create_resource.forms import ResourceForm

# Create your views here.
def home(request):
    all_resources = Resource.objects.all().order_by("-created_date")
    print(messages)
    return render(request, 'index.html', {"all_resources": all_resources})

def update_resource(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES, instance=resource)
        print(request.FILES)
        if form.is_valid():

            form.save()
            return redirect('home')

    else:
        form = ResourceForm(instance=resource)
        return render(request, 'update_resource.html', {'form': form})


def delete_resource(request, pk):
    resource = Resource.objects.filter(pk=pk)
    resource.delete()
    return redirect('home')

