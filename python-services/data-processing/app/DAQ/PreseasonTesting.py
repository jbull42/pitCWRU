import os
import requests
import fastf1 as ff1




def getLastTestResult(year: int, event: int, session: int):
    session = ff1.get_testing_session(2025, 1, 2)
    session.load()
    print(session.results)
    return session.results