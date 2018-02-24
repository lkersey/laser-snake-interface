from flask import Flask, jsonify
import sql

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/temperatures", methods=['GET',])
def temps():
    return jsonify(sql.get_temperatures(1)), 200

if __name__ == '__main__':
    app.run()
