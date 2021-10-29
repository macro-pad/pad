import requests

def open_word():
    print("Open word Postrequest")


def PostToServer():
   url = 'https://hookb.in/dmXzpekjy3Hx8Yjj89jJ'

   data = {
    "name": "John"
    }

   r = requests.post(url, verify=True, json=data)
    
PostToServer()