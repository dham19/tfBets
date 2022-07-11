from django.shortcuts import render
from django.template import loader

# Create your views here.
from django.http import HttpResponse


def index(request):
    
    template = loader.get_template('bets/index.html')
    context = { "items" : [3, 2, 1, 4, 5]
    }
    return HttpResponse(template.render(context, request))