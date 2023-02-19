import jwt
from flask import Flask, request, jsonify
from functools import wraps

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.args.get('token')

        if not token:
            return jsonify({'message': 'Token is missing'}), 401

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Token is invalid'}), 401

        return f(*args, **kwargs)

    return decorated

@app.route('/chatbot')
@token_required
def chatbot():
    request_data = request.get_json()
    message = request_data['message']
    response = return_response(message)
    return jsonify({'response': response})

# Example code for generating a JWT token
@app.route('/login')
def login():
    # Example user credentials (should be validated against a database or other source)
    username = 'user'
    password = 'pass'

    if request.authorization and request.authorization.username == username and request.authorization.password == password:
        payload = {'sub': username}
        token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
        return jsonify({'token': token})

    return make_response('Could not verify!', 401, {'WWW-Authenticate': 'Basic realm="Login Required"'})

if __name__ == '__main__':
    app.run()
