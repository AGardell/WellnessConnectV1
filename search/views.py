from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import WellnessProfessionals
# Create your views here.
def Index(request):
    return render(request, 'search/base.html')

def Search(request):
    zip = request.GET.get('zipcode')
    profs = WellnessProfessionals.objects.filter(zip=zip)
    context = {'professionals': profs, 'zip': zip}
    return render(request, 'search/search.html', context)