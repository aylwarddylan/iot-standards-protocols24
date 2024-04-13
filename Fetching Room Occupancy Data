import requests

def fetch_room_occupancy(api_url):
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        # Assume the API returns a list of rooms with their occupancy status and check-in/check-out times
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to retrieve data: {e}")
        return None
