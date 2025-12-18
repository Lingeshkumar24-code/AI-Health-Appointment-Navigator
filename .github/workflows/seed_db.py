from database import Base, engine, SessionLocal
from models import Doctor

Base.metadata.create_all(bind=engine)

db = SessionLocal()

doctors = doctors = [
    # Cardiology
    Doctor(hospital="Apollo Hospital", specialty="Cardiology",
           doctor_name="Dr. Ramesh Kumar", available_time="Tomorrow 10 AM"),

    # General Physician
    Doctor(hospital="Fortis Hospital", specialty="General Physician",
           doctor_name="Dr. Suresh Rao", available_time="Today 4 PM"),

    # Neurology
    Doctor(hospital="Manipal Hospital", specialty="Neurology",
           doctor_name="Dr. Anita Sharma", available_time="Tomorrow 11 AM"),

    # Gastroenterology
    Doctor(hospital="Aster Hospital", specialty="Gastroenterology",
           doctor_name="Dr. Vijay Malhotra", available_time="Today 6 PM"),

    # Dermatology
    Doctor(hospital="SkinCare Clinic", specialty="Dermatology",
           doctor_name="Dr. Neha Gupta", available_time="Tomorrow 2 PM")
]
db.add_all(doctors)
db.commit()
db.close()

print("Database created and doctors added")
