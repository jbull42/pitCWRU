import requests
import os

baseUrl = os.getenv("OPENF1_URL")

def getLastSessionResults():
    url = baseUrl + "session_result"
    response = requests.get(url, params= { "session_key": "latest" })
    data = response.json()
    return data

def getLastSession():
    url = baseUrl + "sessions"
    response = requests.get(url, params= { "session_key": "latest" })
    data = response.json()
    return data
