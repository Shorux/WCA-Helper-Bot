import json

with open('apiwca/data/countries.json') as file:
    countries = json.load(file)

with open('apiwca//data/continents.json') as file:
    continents = json.load(file)

with open('apiwca//data/events.json') as file:
    events = json.load(file)
