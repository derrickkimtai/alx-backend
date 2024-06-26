#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup
"""
from flask import Flask, render_template
from typing import List, Tuple

app = Flask(__name__)


@app.route('/')
def index():
    """ Main route

    Returns:
        str: template
    """
    return render_template('0-index.html')


if __name__ == '__main__':
    app.run()
