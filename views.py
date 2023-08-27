from flask import Blueprint
import os

views = Blueprint("views", __name__)

@views.route("/")
def home():
    user = os.environ.get('USER_ID')

    if(user):
        return user
    return "<h1>Hello World</h1>"