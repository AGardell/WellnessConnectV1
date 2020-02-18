from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse
from .forms import ContactForm

from .models import WellnessProfessional
# Create your views here.
def Detail(request, prof_id):
    if (request.method == 'POST'):
        contactForm = ContactForm(request.POST)
        if contactForm.is_valid():
            response = HttpResponse("Message Sent!")
            response.status_code = 200
            return response
        else:
            response = HttpResponse(contactForm.as_p())
            response.status_code = 400
            return response
            
    else:
        professional = WellnessProfessional.objects.get(id=prof_id)
        contactForm = ContactForm()
        context = {
            'prof' : professional,
            'contactForm': contactForm
        }
        return render(request, 'prof/detail.html', context)
