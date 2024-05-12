from flask import Flask, render_template, url_for
import os
import random

app = Flask(__name__)

# list of Docker images
images = [
    "1.png",
    "2.png",
    "3.png"
]

@app.route("/")
def index():
    url = url_for('static', filename=random.choice(images))
    return render_template("index.html", url=url)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
