from flask import Flask, render_template
from whatdayisitinnz import day
from datetime import datetime

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html", days=day.DAYS)
    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000, debug=True)