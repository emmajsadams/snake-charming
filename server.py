from flask import Flask, jsonify, request
app = Flask(__name__)

@app.route('/')
def main():
    username = request.args.get('username') or 'fakename'
    test_response = { username: ['bar', 'bar2'] }
    return jsonify(test_response)