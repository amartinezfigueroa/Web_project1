from flask import render_template, redirect, request, session
from functools import wraps


def login_required(f):
    """
	Decorate routes to require login.
	http://flask.pocoo.org/docs/0.12/patterns/viewdecorators/
	"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("id_user") is None:
            return redirect("/iniciosecion")
        return f(*args, **kwargs)
    return decorated_function
