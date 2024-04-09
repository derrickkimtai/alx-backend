#!/usr/bin/env python3
"""Basic Flask app with Basic Babel setup"""
from flask import Flask, render_template, request
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Get locale

    Returns:
        str: locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])

@app.route('/')
def index():
    """Main route

    Returns:
        str: template
    """
    return render_template('2-index.html')

if __name__ == '__main__':
    app.run()
