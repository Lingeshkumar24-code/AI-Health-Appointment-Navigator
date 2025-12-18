from fastapi import FastAPI
from database import SessionLocal
from agent import HealthAgent
from models import Appointment
from fastapi.middleware.cors import CORSMiddleware




app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "AI Health Appointment Navigator is running"}

@app.post("/find-appointment")
def find_appointment(name: str, symptoms: str, city: str):
    db = SessionLocal()
    agent = HealthAgent(db)

    result = agent.run(symptoms, city)

    db.add(Appointment(
        patient_name=name,
        hospital=result["hospital"],
        doctor=result["doctor"],
        time=result["time"]
    ))
    db.commit()

    return result
