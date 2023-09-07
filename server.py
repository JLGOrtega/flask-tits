import os
from flask import Flask, send_from_directory, render_template, redirect, request
from inutils import sorpresa

app = Flask(__name__)

port = int(os.environ.get("PORT", 5000))

@app.route("/", methods=["GET"])
def hello():
    name = "leopoldo"
    if "name" in request.args:
        name = request.args["name"]
    return f"<h1>Hello {name}</h1><br>{sorpresa}"

if __name__ == "__main__":
    app.run(port=port)
