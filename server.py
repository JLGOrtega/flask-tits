import os
from flask import Flask, send_from_directory, render_template, redirect, request, jsonify
from inutils import sorpresa
from sqlalchemy import create_engine
import pandas as pd

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/", methods=["GET"])
def hello():
    name = "leopoldo"
    if "name" in request.args:
        name = request.args["name"]
    return f"<h1>Hello {name}</h1><br>{sorpresa}"

@app.route("/table", methods=["GET"])
def table():
    engine = create_engine("postgresql://fl0user:bleB3zxJy9nN@ep-steep-fire-21690954.eu-central-1.aws.neon.tech:5432/postgres?sslmode=require")
    return jsonify(pd.read_sql_table("test", con=engine).to_dict("records"))

if __name__ == "__main__":
    app.run(port=port)
