#packages
import json
import requests

#funktionen

def json_extract(obj, key):
    """Recursively fetch values from nested JSON."""
    arr = []

    def extract(obj, arr, key):
        """Recursively search for values of key in JSON tree."""
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    values = extract(obj, arr, key)
    return values

#json holen
url = 'https://wttr.in/Darmstadt?format=j1'
r = requests.get(url)
wttr=r.json()

#json in datei schreiben

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(wttr, f, ensure_ascii=False, indent=4)






temps=json_extract(wttr,'FeelsLikeC')
print(temps)

humidity=json_extract(wttr,'humidity')
print('Feuchtigkeit: '+humidity[1]+'%')
