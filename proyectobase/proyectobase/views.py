from fileinput import close
from pipes import Template
from re import template
from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def familia(request):
    return render(request, 'familia.html')

def index(request):
    return render(request, 'index.html')
    