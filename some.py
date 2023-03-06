import requests

url = "https://distance-calculator.p.rapidapi.com/distance/simple"

querystring = {"lat_1": "47.373535", "long_1": "8.541109", "lat_2": "42.335321", "long_2": "-71.023516",
               "unit": "kilometers ", "decimal_places": "0"}

headers = {
    "Content-Type": "application/json",
    "X-RapidAPI-Key": "acdbe594e4msh76247490b0a3bcep1180cdjsnbe75668a06b4",
    "X-RapidAPI-Host": "distance-calculator.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)

import requests

url = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"

querystring = {"address": "Минск", "language": "ru"}

headers = {
    "X-RapidAPI-Key": "acdbe594e4msh76247490b0a3bcep1180cdjsnbe75668a06b4",
    "X-RapidAPI-Host": "google-maps-geocoding.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
response = response.json()
print(response)


d = {'results': [
    {'address_components':
        [
            {'long_name': 'Минск', 'short_name': 'Минск', 'types': ['locality', 'political']},
            {'long_name': 'Минский район', 'short_name': 'Минский район',
             'types': ['administrative_area_level_2', 'political']},
            {'long_name': 'Минская область', 'short_name': 'Минская область',
             'types': ['administrative_area_level_1', 'political']},
            {'long_name': 'Беларусь', 'short_name': 'BY', 'types': ['country', 'political']}],
        'formatted_address': 'Минск, Беларусь',
        'geometry': {'bounds':
                         {'northeast': {'lat': 53.972648, 'lng': 27.8088001},
                          'southwest': {'lat': 53.796632, 'lng': 27.3779368}},
                     'location': {'lat': 53.9006011, 'lng': 27.558972},
                     'location_type': 'APPROXIMATE',
                     'viewport': {
                         'northeast': {'lat': 53.972648, 'lng': 27.8088001},
                         'southwest': {'lat': 53.796632, 'lng': 27.3779368}}},
        'place_id': 'ChIJ02oeW9PP20YR2XC13VO4YQs', 'types': ['locality', 'political']}], 'status': 'OK'}

print(d.get('results')[0].get('geometry').get('location'))