#!/usr/bin/env python3
''' i18n - Basic Flask App
'''
from typing import Dict, Union
from flask import Flask
from flask import render_template
from flask import g, request
from flask_babel import Babel


class Config(object):
    ''' App Configuration class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)

babel = Babel(app)


@babel.localeselector
def get_locale():
    ''' Gets the locale language from request
    '''

    locale = request.args.get('locale', '').strip()
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    locale = g.user.get('locale', '') if g.user else ''
    if locale and locale in app.config["LANGUAGES"]:
        return locale
    if request.accept_languages.best_match(app.config["LANGUAGES"]):
        return request.accept_languages.best_match(app.config["LANGUAGES"])
    return app.config["BABEL_DEFAULT_LOCALE"]


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user(id) -> Union[Dict[str, Union[str, None]], None]:
    ''' Gets a user
    '''
    return users.get(int(id), 0)


@app.before_request
def before_request():
    ''' Sets global variable for logged in user
    '''
    setattr(g, 'user', get_user(request.args.get('login_as', 0)))


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Index route
    '''
    return render_template('6-index.html')


if __name__ == '__main__':
    app.run()
