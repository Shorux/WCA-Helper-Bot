import json

with open('data/countries.json') as file:
    countries = json.load(file)

with open('data/continents.json') as file:
    continents = json.load(file)

with open('data/events.json') as file:
    events = json.load(file)