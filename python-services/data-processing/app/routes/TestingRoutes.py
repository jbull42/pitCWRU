from fastapi import APIRouter
from app.DAQ.PreseasonTesting import getLastTestResult
from datetime import datetime


router = APIRouter()

@router.get("/last-result")
async def get_last_testing_result():
    cur_year = datetime.now().year
    # TODO: include logic to find last session
    results = getLastTestResult(cur_year, 1, 1)

    return results
