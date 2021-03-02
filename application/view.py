from flask import render_template, redirect, request, session, Blueprint, session
from .database import Database
import re
from functools import wraps

view = Blueprint("view", __name__)

def login_required(visit):
    @wraps(visit)
    def login_decorator():
        if "name" in session and "ip" in session:
            print("you are in")
            return visit()
        else:
            print("login required")
            return redirect("/")

    return login_decorator

def session_validation(visit):
    @wraps(visit)
    def session_decorator():
        if "name" in session and "ip" in session:
            print("you are in")
            return redirect("/chat_room")
        else:
            print("login required")
            return visit()

    return session_decorator


@view.route("/")
@session_validation
def home():
    return render_template("home.html")

@view.route("/login", methods=["POST"])
@session_validation
def login():
    if "name" in request.form:
        name = re.sub("[^A-Za-z0-9_@. ]", "", request.form["name"])
        ip = request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

        check = Database.add_user(name, ip)

        if check == True:
            session["name"] = name
            session["ip"] = ip
            return redirect("/chat_room")
        else:
            return redirect(f"/?alert = {check}")

    return redirect("/")

@view.route("/chat_room")
@login_required
def chat_room():
    active_users = Database.ip_users_count(session["ip"])
    return render_template("chat_room.html", active_users = active_users)
        
@view.route("/logout")
@login_required
def logout():
    if "name" in session and "ip" in session:
        check = Database.delete_user(session["name"], session["ip"])

        if check == True:
            session.clear()
            return redirect("/")
        else:
            return redirect(f"/chat_room?alert = {check}")
    return redirect("/chat_room")