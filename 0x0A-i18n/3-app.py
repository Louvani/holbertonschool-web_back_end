#!/usr/bin/env python3
'''Flask app to translate'''

from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    '''Configuration of the language for the app'''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    ''' request.accept_languages to '''
    # user = getattr(g, 'user', None)
    # if user is not None:
    #     return user.locale
    return request.accept_languages.best_match(["en", "fr"])


@app.route('/')
def home():
    '''Home route'''
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
