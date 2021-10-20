#import the necessary package!
import json
import requests
import json

#fetch the weater details
url = 'https://wttr.in/Darmstadt?format=j1'
wttr = requests.get(url)
r=wttr.json()
print(json.dumps(r, indent=2))
print(r['weather'])
for value in r['weather']:
    print(json.dumps(value , indent=2))
    for val in value['hourly']:
        print(val)
        for j in val['humidity']:
            print(j)




 
