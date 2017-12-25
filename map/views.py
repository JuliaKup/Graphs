from django.shortcuts import render
from django.http import HttpResponse
from .models import Station, Route, Line

# Create your views here.


def index(request, template_name='index.html'):
    stations = list(Station.objects.all())
    routes = list(Route.objects.all())
    lines = list(Line.objects.all())

    context = {'stations': stations,
               'routes': routes,
               'lines': lines
               }
    return render(request, template_name, context)

