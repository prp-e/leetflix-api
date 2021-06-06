from flask import Flask, jsonify, request
import search

app = Flask(__name__)

@app.get('/')
def main_endpoint():
    pass

if __name__ == "__main__":
    app.run()