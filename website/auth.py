from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route("/auth")
def login():
    return "<h1>Auth Page</h1>"