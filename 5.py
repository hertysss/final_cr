from flask import Flask, jsonify
from sqlite3 import connect as connect_to_db

PATH = "/schedule"


def get_settings():
    with open("data.txt") as f:
        db_name, year = f.read().split()
        return db_name, year


app = Flask(__name__)


@app.route(PATH)
def solve_task():
    db_name, year = get_settings()
    sql_request = f"""SELECT
id,
name,
load,
crew,
year
FROM spaceships
WHERE year = {year}
ORDER BY load, name
;"""

    connector = connect_to_db(db_name)
    db_data = connector.execute(sql_request).fetchall()
    res_data = list()

    for row in db_data:
        dct = {}
        for key, value in zip(["id", "name", "load", "crew", "year"], row):
            dct[key] = value
        res_data.append(dct)

    return jsonify(res_data)


app.run(host="127.0.0.1", port=5000)