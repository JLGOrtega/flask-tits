from flask import Flask, request
from inutils import sorpresa

app = Flask(__name__)

@app.route("/", methods=["GET"])
def hello():
    name = "leopoldo"
    if "name" in request.args:
        name = request.args["name"]
    return f"<h1>Hello {name}</h1><br>{sorpresa}"


if __name__ ==  "__main__":
    app.run(debug=True)


