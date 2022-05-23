
from pickle import TRUE
from unicodedata import name
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home(name):
    return render_template("index.html", content=["tim", "adda"])


@app.route('/login')
def login():
    return render_template()


@app.route('/<usr')
def user(usr):
    return
# @app.route("/<name>")
# def user(name):
#    return f"hello{name}!"


# @app.route("/admin")
# def admin():
#    return redirect(url_for("user", name="Admin!"))


if __name__ == "__main__":
    app.run(debug=TRUE)
