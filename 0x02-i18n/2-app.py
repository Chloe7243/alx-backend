#!/usr/bin/env python3
''' i18n - Basic Flask App
'''
from flask import Flask
from flask import render_template
from flask import request
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
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/', strict_slashes=False)
def index() -> str:
    ''' Index route
    '''
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run()
