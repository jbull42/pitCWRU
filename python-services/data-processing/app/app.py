from fastapi import FastAPI
from dotenv import load_dotenv
load_dotenv()
from .routes import RaceRoutes

app = FastAPI()

app.include_router(RaceRoutes.router)

@app.get("/")
def home():
    return {"message": "Hello"}