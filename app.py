from flask import Flask, jsonify, request
from flask_jwt_extended import JWTManager, create_access_token

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

@app.route('/')
def home():
    return "Hello, welcome to the homepage!"

@app.route('/login', methods=['POST'])
def login():
    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if username == 'admin' and password == 'password':
        access_token = create_access_token(identity={'username': username})
        return jsonify(access_token=access_token)
    return jsonify({"msg": "Bad credentials"}), 401

@app.route('/status', methods=['GET'])
def status():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(debug=True)
