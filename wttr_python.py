#packages
import json
import requests

#json holen
url = 'https://wttr.in/Darmstadt?format=j1'
r = requests.get(url)
wttr=r.json()
#print(wttr)

currentdate=None

for key in wttr.keys():
    if key == 'current_condition':
        for j in wttr[key]:
         if 'weatherDesc' in j :
             pass
             #print(f"{key}: {j['weatherDesc'][0]['value']}")
    elif key == 'weather':
     for j in wttr[key]:
         if not currentdate:
             currentdate=j['date']
         if 'hourly' in j and currentdate != j['date'] :
             tempc=""
             humi=""
             cor=""
             wd=""
             for i in j['hourly']:
                 tempc+=f"{i['FeelsLikeC']}/"
                 humi+=f"{i['humidity']}/"
                 cor+=f"{i['chanceofrain']}/"
                 wd+=f"{i['weatherDesc'][0]['value']}/"
             print(f"{j['date']}: with temperature {tempc}°C, and {cor} % chance of rain and it's {wd}")
                 

