import os
import requests

baseURL = os.getenv("JOLPICA_URL")

def getDriverStandings(year: int, round: int | str):
    url = baseURL + f"{year}/{round}/driverstandings"
    response = requests.get(url)
    data = response.json()
    drivers = data['MRData']['StandingsTable']['StandingsLists']
    return drivers