# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, reverse
from create_resource.forms import ResourceForm

# Create your views here.
def create_resource(request):

    if request.method == "POST":
        form = ResourceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('home')

    else:
        form = ResourceForm()

    return render(request, 'create_resource.html', {"form": form})
