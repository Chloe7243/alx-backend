#!/usr/bin/env python3
""" Web Flask """
from flask import Flask, render_template


app = Flask(__name__, template_folder="templates")


@app.route("/")
def hello_world():
    """ Hello world """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
