import requests
import configs
import json

def open_word():
    print("Open word Postrequest")


def post_to_server(id, value):
    url = 'http://' + configs.server_ip + ':8000/action/' + id

    data = {
        "value": value
    }

    print(requests.post(url, verify=True, json=data))
    
def get_ui_json():
    url = 'http://' + configs.server_ip + ':8000/grid'

    response = requests.get(url, verify=True)
    return response.json()

# get_ui_configs()