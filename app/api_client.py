import requests
import logging
from .config import API_ENDPOINT

def send_data_to_api(endpoint, data):
    try:
        response = requests.post(f"{API_ENDPOINT}{endpoint}", json=data)
        response.raise_for_status()
        logging.info(f"Data successfully sent to API: {data}")
        return response
    except requests.RequestException as e:
        logging.error(f"Error sending data to API: {e}")
        
def get_data_from_api(endpoint, body=""):
    try:
        url= API_ENDPOINT+endpoint
        print(f"getDataFromAPI {url}")
        response = requests.get(url)
        response.raise_for_status()
        logging.info(f"Data successfully get from API: {response}")
        return response
    except requests.RequestException as e:
        logging.error(f"Error getting data from API: {e}")
