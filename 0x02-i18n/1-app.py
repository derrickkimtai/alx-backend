#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup"""
from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)

class Config:
    """ Config class """
    LANGUAGES = ["en", "fr"]

@app.route('/')
def index():
    """ Main route

    Returns:
        str: template
    """
    return render_template('1-index.html')
