from django.shortcuts import render
from .models import Sequencer
from django.http import HttpResponse
from django.template import loader


def index(request):
    return render(request, 'canetis/index.html')

