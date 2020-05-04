import geopy
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
    ).annotate(distance_lat=Abs(Abs('location_latitude') - Abs(userLocationLatitude))).annotate(distance_long=Abs(Abs('location_longitude') - Abs(userLocationLongitude))
    ).annotate(sum_of_distance=F('distance_lat') + F('distance_long')
    ).order_by('sum_of_distance')

    distance_dict = {}


    for prof in profs:
        distance_dict[prof.id] = round(Decimal(distance.distance((prof.location_latitude, prof.location_longitude), (userLocationLatitude,userLocationLongitude)).miles), 2)

    context = {'professionals': profs, 'distances': distance_dict, 'zip': zip, 'userLat': userLocationLatitude, 'userLong': userLocationLongitude}
    
    #userLocation = geolocator.geocode(zip)
    # profs = WellnessProfessional.objects.filter(
    #     Q(location_latitude__lte=userLocation.latitude + 1) | Q(location_latitude__gte=userLocation.latitude - 1), 
    #     Q(location_longitude__lte=userLocation.longitude + 1) | Q(location_longitude__gte=userLocation.longitude - 1)
    # ).annotate(distance_from_user=distance.distance((userLocation.latitude, userLocation.longitude),(Count('location_latitude'), Count('location_longitude'))).miles)
    #.annotate(distance_from_user=distance.distance((userLocation.latitude, userLocation.longitude),(location_latitude, location_longitude)).miles)
    #profs = profs.annotate(distance_from_user=distance.distance((userLocation.latitude, userLocation.longitude),(location_latitude, location_longitude)).miles)

    #context = {'professionals': profs, 'zip': zip, 'userLat': userLocation.latitude, 'userLong': userLocation.longitude}
    return render(request, 'search/search.html', context)