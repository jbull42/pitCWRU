from fastapi import APIRouter
from app.DAQ.Drivers import getDriverStandings
from datetime import datetime


router = APIRouter()

@router.get("/current-standings")
async def get_current_standings():
    cur_year = datetime.now().year
    standings = getDriverStandings(cur_year, "last")
    if len(standings) == 0:
        standings = getDriverStandings(cur_year - 1, "last")

    return standings[0]["DriverStandings"]
