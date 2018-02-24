from flask import Flask, jsonify
from flask_cors import CORS
import sql

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/", methods=['GET',])
def hello():
    return jsonify("Hello, World!"), 200

@app.route("/temperatures", methods=['GET',])
def temps():
    return jsonify(sql.get_temperatures(1)), 200

if __name__ == '__main__':
    app.run()
