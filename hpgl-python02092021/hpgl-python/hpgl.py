import hpgl
import json

f = open('data.json')

data = json.load(f)

for i in data["P"]:
    print(i)
