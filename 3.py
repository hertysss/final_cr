import json
import sys
import requests
import datetime

DATE, TIME = input().split()
DATE = datetime.datetime.strptime(DATE, '%Y-%m-%d')
TIME = datetime.datetime.strptime(TIME, '%H:%M')

with open("third.json") as serv_file:
    data = json.load(serv_file)

server = data["host"]
port = data["port"]

full_server_url = f"http://{server}:{port}"

response = requests.get(full_server_url, {"format": "json"})

if not response:
    sys.exit()

json_response = response.json()
c_pas = 0
print(json_response)
for js in json_response:
    date = datetime.datetime.strptime(js["date"], '%Y-%m-%d')
    time = datetime.datetime.strptime(js["time"], '%H:%M')
    pas = js["passengers"]
    if (date == DATE and time <= TIME) or date < DATE:
        if js["type"] == "descent":
            c_pas -= pas
        else:
            c_pas += pas
    else:
         break
print(c_pas)