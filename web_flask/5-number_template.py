#!/usr/bin/python3
"""Starts a Flask web application on different routes"""

from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
	"""prints "Hello HBNB!"""
	return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
	"""Prints HBNB on route /hbnb"""
	return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def hello_world_in_c(text: str) -> str:
	"""adds the /c/<text> route"""
	sanitized_text = escape(text).replace('_', ' ')
	return f"C {sanitized_text}"


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_text(text: str = "is cool") -> str:
	"""adds route /python/<text>"""
	sanitized_text = escape(text).replace('_', ' ')
	return f"Python {sanitized_text}"


@app.route("/number/<int:n>", strict_slashes=False)
def is_number(n):
	"""Displays n if n is int"""
	return("{:d} is a number".format(n))


@app.route("/number_template/<int:n>", strict_slashes=False)
def is_number(n):
	"""Renders template if n is int"""
	return render_template('5-number.html', n=n)


if __name__ == "__main__":
	app.run(host="0.0.0.0", port="5000")
