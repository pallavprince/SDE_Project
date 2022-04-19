from django.shortcuts import render, redirect
from django.conf import settings


def scan_history(request, id):
    scanid = id
    context = {}
    
    return render(request, "orascan/scan_history.html", context)


def history(request):
    context = {}
    return render(request, "orascan/history.html", context)


def home(request):
    context = {}
    return render(request, "orascan/index.html", context)
