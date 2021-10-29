import requests
import configs
import json

def open_word():
    print("Open word Postrequest")


def post_to_server():
   url = 'https://hookb.in/dmXzpekjy3Hx8Yjj89jJ'

   data = {
    "name": "John"
    }

   requests.post(url, verify=True, json=data)
    
def get_ui_configs():
   url = 'http://' + configs.server_ip + ':8000/grid'

   response = requests.get(url, verify=True)
   grid = response.json()
   print(grid["buttons"]["2"]["name"])

# get_ui_configs()