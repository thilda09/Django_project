from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    text = """<h1>Bienvenue sur mon site</h1>
    <p>Ce site est un tableau de bord d'un Hotel :) </p>"""
    return HttpResponse(text)
