import requests

def set_target_temperature(serial_number, temperature, access_token, api_host):
    url = f"http://{api_host}/provider/send"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {access_token}"
    }
    payload = {
        "serial_number": serial_number,
        "command": "set_target_temperature",
        "temp": temperature
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

