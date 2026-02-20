from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from .routes import RaceRoutes
from .routes import ConstructorRoute

app = FastAPI()

app.include_router(RaceRoutes.router)
app.include_router(ConstructorRoute.router, prefix="/constructors")

@app.get("/")
def home():
    return {"message": "Hello"}