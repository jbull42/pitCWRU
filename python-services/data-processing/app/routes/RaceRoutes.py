from fastapi import APIRouter
from app.DAQ import Races, LastSession

router = APIRouter()

@router.get("/races", tags=['races'])
async def read_race_names():
    return Races.getCurrentRaceYearNames()

@router.get("/res")
async def test():
    return LastSession.getLastSessionResults()

@router.get("/res2")
async def test2():
    return LastSession.getLastSession()
