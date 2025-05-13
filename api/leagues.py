import os
import requests
from dotenv import load_dotenv

load_dotenv()

class LeaguesEndpoint:
    def __init__(self):
        self.base_url = os.getenv("API_BASE_URL")
        self.api_key = os.getenv("API_KEY")

    def get_data(self, country):
        url = f"{self.base_url}/leagues"
        headers = {
            "x-apisports-key": self.api_key
        }
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            data = response.json()["response"]
            return [league for league in data if league["country"]["name"].lower() == country.lower()]
        else:
            return []
