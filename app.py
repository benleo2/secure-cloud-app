from flask import Flask
import logging

app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    app.logger.info("Homepage accessed")
    return "Secure Cloud App Running"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)

import os

secret = os.gentnv("APP_MODE")

print(secret)

from flask_talisman import Talisman

Talisman(app)

@app.route("/health")
def health():
    return {"status":"healthy"}
