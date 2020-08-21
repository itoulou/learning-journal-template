# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404, redirect
from create_resource.models import Language, Framework, Database, Technology
from software.forms import LanguageForm, DatabaseForm, FrameworkForm, TechnologyForm

# Create your views here.
def view_languages(request):
    choices = Language.objects.filter()
    return render(request, 'languages.html', {"choices": choices})

def create_or_edit_language(request, pk=None):
    language = get_object_or_404(Language, pk=pk) if pk else None
    if request.method == "POST":
        form = LanguageForm(request.POST, instance=language)
        if form.is_valid():
            form.save()
            return redirect('languages')
    else:
        form = LanguageForm(instance=language)
        return render(request, 'software_form.html', {"form": form, "software": "Language"})


def delete_language(request, pk):
    language = get_object_or_404(Language, pk=pk)
    language.delete()
    return redirect('languages')


def view_frameworks(request):
    choices = Framework.objects.filter()
    return render(request, 'frameworks.html', {"choices": choices})

def create_or_edit_framework(request, pk=None):
    framework = get_object_or_404(Framework, pk=pk) if pk else None
    if request.method == "POST":
        form = FrameworkForm(request.POST, instance=framework)
        if form.is_valid():
            form.save()
            return redirect('frameworks')
    else:
        form = FrameworkForm(instance=framework)
        return render(request, 'software_form.html', {"form": form, "software": "Framework"})

def delete_framework(request, pk):
    framework = get_object_or_404(Framework, pk=pk)
    framework.delete()
    return redirect('frameworks')


def view_databases(request):
    choices = Database.objects.filter()
    return render(request, 'databases.html', {"choices": choices})

def create_or_edit_database(request, pk=None):
    database = get_object_or_404(Database, pk=pk) if pk else None
    if request.method == "POST":
        form = DatabaseForm(request.POST, instance=database)
        if form.is_valid():
            form.save()
            return redirect('databases')
    else:
        form = DatabaseForm(instance=database)
        return render(request, 'software_form.html', {"form": form, "software": "Database"})

def delete_database(request, pk):
    database = get_object_or_404(Database, pk=pk)
    database.delete()
    return redirect('databases')

def view_technologies(request):
    choices = Technology.objects.filter()
    return render(request, 'technologies.html', {"choices": choices})

def create_or_edit_technology(request, pk=None):
    technology = get_object_or_404(Technology, pk=pk) if pk else None
    if request.method == "POST":
        form = TechnologyForm(request.POST, instance=technology)
        if form.is_valid():
            form.save()
            return redirect('technologies')
    else:
        form = TechnologyForm(instance=technology)
        return render(request, 'software_form.html', {"form": form, "software": "Technology"})

def delete_technology(request, pk):
    technology = get_object_or_404(Technology, pk=pk)
    technology.delete()
    return redirect('technologies')





