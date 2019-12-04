from flask import Flask, render_template, session, request, redirect, url_for
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key = "cmYU7dj*dd&U7p&95j53gv8iCF6fPaTac$ZEcfoN^uBqxH"
login_manager = LoginManager(app)

users = {
    "julian": {
        "username": "julian",
        "email": "julian@gmail.com",
        "password": "example",
        "bio": "Some guy from the internet"
    },
    "clarissa": {
        "username": "clarissa",
        "email": "clarissa@icloud.com",
        "password": "sweetpotato22",
        "bio": "Sweet potato is life"
    }
}

@app.route("/", methods=['GET', 'POST'])
def home():
    return render_template("index.html", title="Login")

@app.route("/interfaces")
def interfaces():
    return render_template("interfaces.html", title="Interfaces")

@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():
    if request.method == "POST":
        req = request.form
        username = req.get("username")
        password = req.get("password")
        if not username in users:
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]
        if not password == user["password"]:
            print("Incorrect password")
            return redirect(request.url)
        else:
            session["USERNAME"] = user["username"]
            print("session username set")
            return redirect(url_for("profile"))

    return render_template("interfaces.html", title="Interfaces")

if __name__ == '__main__':
    app.run(debug=True)
