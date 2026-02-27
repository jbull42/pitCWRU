from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from .routes import RaceRoutes
from .routes import ConstructorRoute
from .routes import DriverRoute
from .routes import TestingRoutes

app = FastAPI()

app.include_router(RaceRoutes.router)
app.include_router(ConstructorRoute.router, prefix="/constructors")
app.include_router(DriverRoute.router, prefix='/drivers')
app.include_router(TestingRoutes.router, prefix='/testing')

@app.get("/")
def home():
    return {"message": "Hello"}