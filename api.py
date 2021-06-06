from flask import Flask, json, jsonify, request
import search

app = Flask(__name__)

@app.post('/')
def main_endpoint():
    data = request.get_json()
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)