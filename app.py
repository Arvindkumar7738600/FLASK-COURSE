from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")


@app.route("/submit", methods=["POST"])
def login():
    username = request.form["username"]
    password = request.form["password"]

    if username == "arvindk." and password == "pass":
        return redirect(url_for("welcome", username=username))
    else:
        return "Invalid Credentials"


@app.route("/welcome/<username>")
def welcome(username):
    return render_template("welcome.html", username=username)


if __name__ == "__main__":
    app.run(debug=False, port=5500)