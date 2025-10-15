from flask import Flask, render_template, jsonify
from ActividadListasCircularesDobles import ClockStructure
import threading
import time

app = Flask(__name__)
clock = ClockStructure()

def run_clock():
    while True:
        clock.tick()
        time.sleep(1)

thread = threading.Thread(target=run_clock, daemon=True)
thread.start()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/time")
def get_time():
    hour, minute, second = clock.get_time()
    return jsonify({
        "hour": hour,
        "minute": minute,
        "second": second
    })

if __name__ == "__main__":
    app.run(debug=True)


