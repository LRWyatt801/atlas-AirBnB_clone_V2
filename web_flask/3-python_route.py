#!/usr/bin/python3
"""Starts a Flask web application on different routes"""

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints "Hello HBNB!"

    Returns:
        string: printed script
    """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints HBNB on route /hbnb

    Returns:
        str: return string
    """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world_in_c(text: str) -> str:
    """adds the /c/<text> route

    Args:
        text (str): text to return

    Returns:
        str: sanitized text
    """
    sanitized_text = escape(text).replace('_', ' ')
    return f"C {sanitized_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text: str = "is cool") -> str:
    """adds route /python/<text>

    Args:
        text (str, optional): text to display. Defaults to "is cool".

    Returns:
        str: returns str of input text
    """
    sanitized_text = escape(text).replace('_', ' ')
    return f"Python {sanitized_text}"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
