# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hello(request):
    return HttpResponse("Hello world ! ")

def test(request):
    return render(request, 'test.html')

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

def contact(request):
    return render(request, 'contact.html')

# Portfolio
def portfolio_1_col(request):
    return render(request, 'portfolio-1-col.html')

# Other Pages
def full_width(request):
    return render(request, 'full-width.html')

def sidebar(request):
    return render(request, 'sidebar.html')
def faq(request):
    return render(request, 'faq.html')
def pokyu404(request):
    return render(request, '404.html')
def pricing(request):
    return render(request, 'pricing.html')


