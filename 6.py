import csv
import json
import sqlite3
import sys

import requests

#1
data = [i for i in sys.stdin.read().split()]

# открыть json-файл
with open(filename) as serv_file:
    data = json.load(serv_file)


# Сделать запрос на сервер и получить данные
full_server_url = f"http://{server}:{port}"

response = requests.get(full_server_url, {"format": "json"})

if not response:
    sys.exit()

json_response = response.json()
#for js in json_response:
#    date = datetime.datetime.strptime(js["date"], '%Y-%m-%d')
 #   time = datetime.datetime.strptime(js["time"], '%H:%M')
#    pas = js["passengers"]
#    if (date == DATE and time <= TIME) or date < DATE:
#        if js["type"] == "descent":
#            c_pas -= pas
#       else:
#           c_pas += pas
 #   else:
 #        break




# получение данных из сsv-файла
with open(filename, encoding="utf8") as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',', quotechar='"')
    for dct in reader:
        pass


# записать в json-файл
def write_data(filename, data):
    with open(filename, 'w') as f:
        json.dump(data, f)


# подключение к таблице и написание запроcа
db = input()
title, loophole_number = input().split()
con = sqlite3.connect(db)
res = con.cursor().execute(f"""SELECT team.name, team.weapon, schedule.time_on_duty from schedule
LEFT JOIN places_to_protect ON place_id = places_to_protect.id
LEFT JOIN team ON team_id = team.id
WHERE schedule.loophole_number = '{loophole_number}'
AND places_to_protect.title = '{title}'
ORDER BY schedule.time_on_duty""").fetchall()
con.close()
with open(filename, "w", newline='') as f:
    writer = csv.writer(f, delimiter=';', quotechar='"')
    for i in res:
        writer.writerow(i)


# создание приложения flask
from flask import Flask, jsonify
from sqlite3 import connect as connect_to_db

PATH = "/experiments"


def get_settings():
    filename = filename
    with open(filename) as in_f:
        db_name, min_rel = in_f.read().split("\n")
        return db_name, min_rel


app = Flask(__name__)


@app.route(PATH)
def solve_task():
    db_name, min_rel = get_settings()
    sql_request = f"""SELECT
laboratory,
mass,
exceeding,
time
FROM experiments
WHERE reliability >= {min_rel}
ORDER BY time, mass, exceeding
;"""

    connector = connect_to_db(db_name)
    db_data = connector.execute(sql_request).fetchall()
    res_data = dict()

    for row in db_data:
        key, *ost = row
        if key not in res_data:
            res_data[key] = list()
        res_data[key].append(list(ost))

    #    for row in db_data:
    #    dct = {}
    #    for key, value in zip(["id", "name", "load", "crew", "year"], row):
    #        dct[key] = value
    #    res_data.append(dct)

    return jsonify(res_data)


app.run(host="127.0.0.1", port=5000)



