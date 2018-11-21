from math import sin, cos, sqrt
from geopy import distance
from django.contrib.auth.models import User
from django.conf import settings
from pages.models import Profile
from urllib.parse import urljoin
import requests

# get user's location via IP and returns info in a dictionary 
def getLocation():
    response = requests.get(urljoin('http://api.ipstack.com/', 'check?access_key=' + settings.IP_STACK_ACCESS_KEY))
    geodata = response.json()
    return geodata

# returns a list of people nearby in a something mi radius
def getNearby(user, radius, distList=None, age=None):
    myProfile = user.profile
    profiles = Profile.objects.exclude(user = user).all()

    if age is not None:
        profiles = profiles.filter(age__lte=age)

    nearbyPeople = []

    meLoc = (myProfile.latitude, myProfile.longitude)

    if profiles is not None:
        for profile in profiles:
            userLoc = (profile.latitude, profile.longitude)
            if all(userLoc):
                length = distance.distance(meLoc, userLoc).miles
                if length < radius:
                    nearbyPeople.append(profile)
                    if distList is not None:
                        distList.append('%.2f'%(round(length,1)))
    
    return nearbyPeople