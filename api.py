from flask import Flask, json, jsonify, request
from flask_cors import CORS
import search

app = Flask(__name__)
cors = CORS(app)

@app.post('/')
def main_endpoint():
    input_data = request.get_json()
    keyword = input_data['keyword']
    data = search.gather_data(keyword)

    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)