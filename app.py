# from database.db_connection import connect_collection
from flask import Flask, render_template, request, redirect, url_for, flash, session
from logging import FileHandler, WARNING

app = Flask(__name__, template_folder="template")
# collection = connect_collection("ingredients")


@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        if request.form.get("action1") == "breakfast":
            return "OK"  # redirect(url_for("breakfast"))
        else:
            return "Not OK"  # redirect(url_for("dinner"))
    return render_template("home.html")


# @app.route("/dinner", methods=["GET", "POST"])
# def dinner():

if __name__ == "__main__":
    app.debug = True
    app.run()
