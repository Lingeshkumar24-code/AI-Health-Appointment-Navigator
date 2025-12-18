import requests

def find_nearby_hospitals(city):
    url = "https://nominatim.openstreetmap.org/search"
    params = {
        "q": f"hospital in {city}",
        "format": "json",
        "limit": 3
    }
    headers = {"User-Agent": "health-ai-agent"}

    response = requests.get(url, params=params, headers=headers)
    data = response.json()

    return [place["display_name"].split(",")[0] for place in data]
