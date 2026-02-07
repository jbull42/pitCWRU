import os
import requests

baseUrl = os.getenv("JOLPICA_URL")

def getCurrentRaceYearNames():
    url = baseUrl + "current/races"
    response = requests.get(url)
    data = response.json()
    races = data['MRData']['RaceTable']['Races']
    race_list = [race['raceName'] for race in races]
    return race_list