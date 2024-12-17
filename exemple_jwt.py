from flask import Flask, jsonify
import jwt
from datetime import datetime, timedelta, timezone


app = Flask(__name__)


@app.route("/", methods=["POST"])
def login():
    token = jwt.encode(
        payload={"exp": datetime.now(timezone.utc) + timedelta(minutes=1)},
        key="minhaChave",
        algorithm="HS256",
    )
    return jsonify({"token": token}), 200


@app.route("/secret", methods=["POST"])
def secret():
    return jsonify({"meu": "segredo"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
