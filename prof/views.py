from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from django.contrib import messages
from .forms import ContactForm

from .models import WellnessProfessional
# Create your views here.
def Detail(request, prof_id):
    professional = WellnessProfessional.objects.get(id=prof_id)

    if (request.method == 'POST'):
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            return JsonResponse({'success':True})
        else:
            return JsonResponse({'error':contactForm.errors})
    else:
        contactForm = ContactForm()
    
    context = {
        'prof' : professional,
        'contactForm': contactForm
    }
    return render(request, 'prof/detail.html', context)
