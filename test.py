from flask import Flask, jsonify

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify([
  {"date": "2023-04-01", "time": "08:30", "type": "ascent", "passengers": 90},
  {"date": "2023-04-01", "time": "18:30", "type": "descent", "passengers": 50},
  {"date": "2023-04-01", "time": "20:00", "type": "descent", "passengers": 40},
  {"date": "2023-04-02", "time": "08:30", "type": "ascent", "passengers": 100},
  {"date": "2023-04-02", "time": "09:00", "type": "descent", "passengers": 85},
  {"date": "2023-04-02", "time": "09:30", "type": "ascent", "passengers": 90},
  {"date": "2023-04-02", "time": "10:45", "type": "ascent", "passengers": 120},
  {"date": "2023-04-02", "time": "12:15", "type": "descent", "passengers": 235}
])


app.run(host="127.0.0.1", port=5000)