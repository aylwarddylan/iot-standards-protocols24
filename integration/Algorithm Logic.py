import requests

def fetch_rooms(host_name, hotel_id, token):
    # Fetches room status from Opera Cloud API
    url = f"https://{host_name}/fof/v1/hotels/{hotel_id}/rooms"
    headers = {
        'Authorization': f'Bearer {token}', # specific authorization access required
        'Content-Type': 'application/json'
    }
    params = {
        'roomType': 'SUP',  # Sample room type
        'hotelRoomStatus': 'Inspected',
        'hotelRoomFrontOfficeStatus': 'Vacant'  # fetching vacant rooms
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def set_target_temperature(serial_number, temperature, access_token, api_host):
    # Sets the target temperature for a room using the Vicki API
    url = f"https://{api_host}/provider/send"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}" # specific authorization access required
    }
    # MCLimate API push
    payload = {
        "serial_number": serial_number,
        "command": "set_target_temperature",
        "temp": temperature,
        "room_id": "example_room_id",  # Replace with actual room ID
        "event": "room_booked"  # Context of the event
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

def main():
    # Configuration variables
    host_name = "example.com" 
    hotel_id = "1234"
    opera_token = "opera_access_token"
    vicki_token = "vicki_access_token"
    api_host = "mclimate_api_host"
    
    # Fetch rooms
    rooms = fetch_rooms(host_name, hotel_id, opera_token)
    
    # Process each room's status
    for room in rooms.get('rooms', []):
        serial_number = room.get('serial_number')  # Ensure this key exists in data
        room_status = room.get('hotelRoomFrontOfficeStatus')
        
        # Define temperatures based on status
        if room_status == 'Vacant':
            temperature = 16  # Lower temperature for energy saving
        else:
            temperature = 22  # Comfortable temperature for guests
        
        # Set the target temperature using Vicki API
        response = set_target_temperature(serial_number, temperature, vicki_token, api_host)
        print(f"Set temperature for room {room['room_id']} to {temperature}°C: {response}")

if __name__ == "__main__":
    main()
