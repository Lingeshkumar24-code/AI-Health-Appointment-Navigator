# 🏥 AI Health Appointment Navigator

An AI-powered healthcare appointment recommendation system built using **FastAPI**, **SQLite**, **SQLAlchemy**, and **OpenStreetMap APIs**. It helps users find the right medical specialist and a nearby hospital based on their symptoms.

## Features

- Symptom-based specialty recommendation
- Nearby hospital search using OpenStreetMap
- Doctor recommendation from a local database
- Appointment recording in SQLite
- REST API built with FastAPI
- Responsive web interface

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Requests
- HTML/CSS
- OpenStreetMap Nominatim API

## Project Structure

```
AI-Health-Appointment-Navigator/
│
├── main.py
├── agent.py
├── database.py
├── models.py
├── tools.py
├── seed_db.py
├── health.db
├── main.html
└── ai Project Report.pdf
```

## Workflow

1. User enters name, symptoms, and city.
2. The AI agent maps symptoms to a medical specialty.
3. Nearby hospitals are fetched from OpenStreetMap.
4. The database is searched for an available doctor.
5. Appointment details are saved.
6. Results are returned to the user.

## API

### GET /

Returns the application status.

### POST /find-appointment

Parameters:

- `name`
- `symptoms`
- `city`

Example Response

```json
{
  "hospital": "Apollo Hospital",
  "doctor": "Dr. Ramesh Kumar",
  "time": "Tomorrow 10 AM"
}
```

## Installation

```bash
git clone https://github.com/Lingeshkumar24-code/AI-Health-Appointment-Navigator.git
cd AI-Health-Appointment-Navigator
```

Install dependencies:

```bash
pip install fastapi uvicorn sqlalchemy requests
```

Create the database:

```bash
python seed_db.py
```

Run the server:

```bash
uvicorn main:app --reload
```

Open:

```
http://127.0.0.1:8000
```

## Future Improvements

- LLM-powered symptom understanding
- RAG with medical documents
- Live hospital appointment integration
- User authentication
- Doctor ratings and recommendations
- Voice-based symptom input
- Medical report upload and analysis

## Author

**Lingesh Kumar M**
