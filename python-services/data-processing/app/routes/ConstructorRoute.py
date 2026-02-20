from fastapi import APIRouter
from app.DAQ.Constructors import getConstructorStandings
from datetime import datetime

router = APIRouter()

@router.get("/current-standings")
async def get_current_standings():
    cur_year = datetime.now().year
    standings = getConstructorStandings(cur_year, "last")
    if len(standings) == 0:
        standings = getConstructorStandings(cur_year - 1, "last")

    return standings[0]["ConstructorStandings"]

@router.get("/standings")
async def get_standings_by_year_round(year: int, round: int):
    try:
        standings = getConstructorStandings(year, round)
        return standings[0]["ConstructorStandings"]
    except:
        return { "Error": "Invalid Parameters" }
