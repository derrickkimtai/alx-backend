#!/usr/bin/env python3
"""Basic Flask app with Basic Babel setup"""
from flask import Flask, render_template, request, g
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"

@babel.localeselector
def get_locale():
    """ Get locale

    Returns:
        str: locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'].keys())


@app.route('/')
def index():
    """ Main route

    Returns:
        str: template
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run()