#!/usr/bin/env python3
'''Flask app to translate'''

from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    '''Configuration of the language for the app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


def get_user():
    '''Return an user by ID'''
    id = request.args.get("login_as")
    if id is not None:
        return users.get(int(id))
    return None


@app.before_request
def before_request():
    '''find a user if any, and set it as a global'''
    user = get_user()
    if user is not None:
        g.user = user


@babel.localeselector
def get_locale():
    ''' request.accept_languages to '''
    lang = request.args.get("locale")
    if lang is not None:
        if lang in Config.LANGUAGES:
            return lang
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def home():
    '''Home route'''
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
