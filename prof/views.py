from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.
def Detail(request, prof_id):
    return render(request, 'prof/detail.html')
