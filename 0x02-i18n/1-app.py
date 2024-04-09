#!/usr/bin/env python3
""" Web Flask """
from flask import Flask, render_template
from flask_babel import Babel


class Config:
    ''' App Configuration class
    '''
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)
babel = Babel(app)


@app.route("/", strict_slashes=False)
def hello_world():
    """ Hello world """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run()
