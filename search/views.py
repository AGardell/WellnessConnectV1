import geopy
import operator

from geopy.geocoders import Nominatim
from geopy import distance

from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point

from django.shortcuts import render
from django.template import loader
from django.db.models import Q, F, Count, Value
from django.db.models.functions import Abs
from django.http import HttpResponse

from decimal import *


from prof.models import WellnessProfessional
# Create your views here.
def Index(request):
    return render(request, 'search/base.html')

def Search(request):
    geolocator = Nominatim(user_agent='wellnessmatchv1')

    zip = request.GET.get('zipcode')

    userLocation = geolocator.geocode(zip)
    #userLocationLatitude = 39.996160
    #userLocationLongitude = -74.947890
    userLocationLatitude = userLocation.latitude
    userLocationLongitude = userLocation.longitude
    userPnt = Point(userLocationLongitude,userLocationLatitude)

    profs = WellnessProfessional.objects.filter(
        Q(location_latitude__lte=userLocationLatitude + 1) | Q(location_latitude__gte=userLocationLatitude - 1), 
        Q(location_longitude__lte=userLocationLongitude + 1) | Q(location_longitude__gte=userLocationLongitude - 1)
    )

    for prof in profs:
        prof.miles = round(Decimal(distance.distance((prof.location_latitude, prof.location_longitude), (userLocationLatitude,userLocationLongitude)).miles), 2)
    
    # need to fix magic number here!
    profs_sorted_filters = list(filter(lambda prof: prof.miles < 1000, sorted(profs, key=operator.attrgetter("miles"))))

    context = {'professionals': profs_sorted_filters, 
        'zip': zip, 
        'userLat': userLocationLatitude, 
        'userLong': userLocationLongitude}
    
    return render(request, 'search/search.html', context)