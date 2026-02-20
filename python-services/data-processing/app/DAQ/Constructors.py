import os
import requests

baseURL = os.getenv("JOLPICA_URL")

def getConstructorStandings(year: int, round: int | str):
    url = baseURL + f"{year}/{round}/constructorstandings"
    response = requests.get(url)
    data = response.json()
    constructors = data['MRData']['StandingsTable']['StandingsLists']
    return constructors