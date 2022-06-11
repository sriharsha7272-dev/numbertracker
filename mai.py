from time import strptime
import phonenumbers
import datetime
from test import phonenumber
from phonenumbers import timezone
from phonenumbers import geocoder
ch_nmbr = phonenumbers.parse(phonenumber, "CH")
print(geocoder.description_for_number(ch_nmbr, "en"))

from phonenumbers import carrier
service_nmbr = phonenumbers.parse(phonenumber, "RO")
print(carrier.name_for_number(service_nmbr, "en"))

time = phonenumbers.parse(phonenumber)
timeZone = timezone.time_zones_for_number(time)
print(time)
print(timeZone)
now = datetime.datetime.now()
print("Current date and time: ")
print(str(now))

from opencage.geocoder import OpenCageGeocode
key ="252956339da1418496ba97f53ba27a7e"
geocoder = OpenCageGeocode(key)
query = str(service_nmbr)
result = geocoder.geocode(query)
print(result)