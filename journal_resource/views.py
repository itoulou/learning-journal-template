# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import boto3
from pathlib import Path
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from create_resource.models import Resource
from create_resource.forms import ResourceForm
from journal.settings import AWS_STORAGE_BUCKET_NAME, AWS_S3_REGION_NAME, AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY

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

def download_attachment(request, pk):
    resource = get_object_or_404(Resource, pk=pk)
    s3 = boto3.resource('s3')
    s3.Bucket(AWS_STORAGE_BUCKET_NAME).download_file('media/' + str(resource.attachment), str(Path.home()) + '/' + str(resource.filename()))
    messages.success(request, 'File {} downloaded'.format(resource.filename()))
    return redirect('home')
