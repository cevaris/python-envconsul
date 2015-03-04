from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    resposne = []
    for name in dir(settings):
        resposne.append("{}: {}<br/>".format(name, getattr(settings, name)))
    return HttpResponse(resposne)
