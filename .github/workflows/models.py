from sqlalchemy import Column, Integer, String, Text
from database import Base

class Doctor(Base):
    __tablename__ = "doctors"
    id = Column(Integer, primary_key=True)
    hospital = Column(String)
    specialty = Column(String)
    doctor_name = Column(String)
    available_time = Column(String)

class Appointment(Base):
    __tablename__ = "appointments"
    id = Column(Integer, primary_key=True)
    patient_name = Column(String)
    hospital = Column(String)
    doctor = Column(String)
    time = Column(String)

class AgentLog(Base):
    __tablename__ = "agent_logs"
    id = Column(Integer, primary_key=True)
    thought = Column(Text)
    action = Column(Text)
    observation = Column(Text)
