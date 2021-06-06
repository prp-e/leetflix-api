from flask import Flask, json, jsonify, request
import search

app = Flask(__name__)

@app.post('/')
def main_endpoint():
    input_data = request.get_json()
    keyword = input_data['keyword']
    data = search.gather_data(keyword)
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)