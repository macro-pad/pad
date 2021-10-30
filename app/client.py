import requests
import configs

def open_word():
    print("Open word Postrequest")


def post_to_server(id, value):
    url = 'http://' + configs.server_ip + ':8000/action/' + id

    data = {
        "value": value
    }

    print(data)

    print(requests.post(url, verify=True, json=data))
    
def redirect_to_ui(id):
    url = 'http://' + configs.server_ip + ':8000/action/' + id

    data = {
        "value": 1
    }

    response = requests.post(url, verify=True, json=data)
    return response.json()

def get_ui_json():
    url = 'http://' + configs.server_ip + ':8000/grid'

    response = requests.get(url, verify=True)
    return response.json()
