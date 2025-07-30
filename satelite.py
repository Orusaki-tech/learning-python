# in this program, we use the requests library to get the number of people in space, 

import requests

response = requests.get('http://api.open-notify.org/astros.json')
print(response)

json = response.json()

# print(json)
print('The people currently in space are?')
for people in json['people']:
    print(people['name'])