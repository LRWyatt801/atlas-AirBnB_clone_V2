#!/usr/bin/python3
"""Start of flask tasks"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """prints "Hello HBNB!"

    Returns:
        string: printed script
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
