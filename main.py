import phonenumbers
from phonenumbers import geocoder,carrier
from secret import NUMBER,API_KEY
from opencage.geocoder import OpenCageGeocode
import folium

#Country Location
x=phonenumbers.parse(NUMBER,None)
location=geocoder.description_for_number(x,"en")
print(location)

#SIM Operator name
operator_name=phonenumbers.parse(NUMBER,"RO")
data=carrier.name_for_number(operator_name,"en")
print(data)

geocoder=OpenCageGeocode(API_KEY)
query=str(location)
result=geocoder.geocode(query)
#print(result)

lat=result[0]['geometry']['lat']
lng=result[0]['geometry']['lng']
print(lat,lng)

my_map=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng], popup=location).add_to(my_map)
my_map.save("Tracker.html")