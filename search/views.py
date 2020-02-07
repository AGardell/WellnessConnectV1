from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Index(request):
    return render(request, 'search/base.html')