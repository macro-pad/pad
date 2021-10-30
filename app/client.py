import requests
import configs

def get_server_url():
    return 'http://' + configs.server_host + ':' + str(configs.server_port) + "/"

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

def get_json_field(id, filed_name):
    url = get_server_url() + "action/" + id

    data = {
        "value": filed_name
    }

    response = requests.post(url, verify=True, json=data)
    return response.text