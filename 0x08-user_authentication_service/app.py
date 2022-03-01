#!/usr/bin/env python3
"""User Authentcation Service"""
from flask import Flask, abort, jsonify, redirect, request

from auth import Auth

AUTH = Auth()

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/', methods=['GET'])
def start():
    """ GET / welcome message
    """
    return jsonify({"message": "Bienvenue"}), 200


@app.route('/users', methods=['POST'])
def register():
    """ POST /users
    Return:
      - 'user created' if success
      - 400 - 'email already registered' if email already
      registered
    """
    email = request.form.get('email')
    password = request.form.get('password')
    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except Exception:
        return jsonify({"message": "email already registered"}), 400


@app.route('/sessions', methods=['POST'])
def login():
    """ POST /sessions
    Return:
      - logged in if success
      - 401 if login info is incorrect
    """
    email = request.form.get('email')
    password = request.form.get('password')
    if not AUTH.valid_login(email, password):
        abort(401)
    session_id = AUTH.create_session(email)
    response = jsonify({"email": email, "message": "logged in"})
    response.set_cookie('session_id', session_id)
    return response


@app.route('/sessions', methods=['DELETE'])
def logout():
    """ DELETE /sessions
    Return:
      - end session and redirect to GET /
      - 403 if user doesn't exist
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        AUTH.destroy_session(user.id)
        return redirect('/')
    else:
        abort(403)


@app.route('/profile', methods=['GET'])
def profile():
    """ GET /profile
    Return:
      - user email
      - 403 if user doesn't exist
    """
    session_id = request.cookies.get('session_id')
    user = AUTH.get_user_from_session_id(session_id)
    if user:
        return jsonify({"email": user.email}), 200
    else:
        abort(403)


@app.route('/reset_password', methods=['POST'])
def get_reset_password_token():
    """ POST /reset_password
    Return:
      - reset token
      - 403 if email isn't registered
    """
    try:
        email = request.form.get('email')
        reset_token = AUTH.get_reset_password_token(email)
        return jsonify({"email": email, "reset_token": reset_token}), 200
    except Exception:
        abort(403)


@app.route('/reset_password', methods=['PUT'])
def update_password():
    """ PUT /reset_password
    Return:
      - update password
      - 403 if token is invalid
    """
    try:
        email = request.form.get('email')
        reset_token = request.form.get('reset_token')
        new_password = request.form.get('new_password')
        AUTH.update_password(reset_token, new_password)
        return jsonify({"email": email, "message": "Password updated"}), 200
    except Exception:
        abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
