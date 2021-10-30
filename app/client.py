import requests
import configs

def get_server_url():
    return 'http://' + configs.server_ip + ':8000/'

def post_to_server(id, value):
    url = get_server_url() + "action/" + id

    data = {
        "value": value
    }

    requests.post(url, verify=True, json=data)
    
def redirect_to_ui(id):
    url = get_server_url() + "action/" + id

    data = {
        "value": 1
    }

    response = requests.post(url, verify=True, json=data)
    return response.json()

def get_ui_json():
    url = get_server_url() + "grid"

    response = requests.get(url, verify=True)
    return response.json()

def get_string(id):
    url = get_server_url() + "action/" + id

    data = {
        "value": 1
    }

    response = requests.post(url, verify=True, json=data)
    return response.text