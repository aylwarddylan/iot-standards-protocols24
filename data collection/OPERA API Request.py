import requests

def fetch_rooms(host_name, hotel_id, token):
    url = f"https://{host_name}/fof/v1/hotels/{hotel_id}/rooms"
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    params = {
        'roomType': 'SUP',
        'hotelRoomStatus': 'Inspected',
        'hotelRoomFrontOfficeStatus': 'Vacant'
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

# criteria reuqired for data collection
host_name = "example.com"
hotel_id = "1234"
token = "your_oauth_token_here"
rooms = fetch_rooms(host_name, hotel_id, token)
print(rooms)

