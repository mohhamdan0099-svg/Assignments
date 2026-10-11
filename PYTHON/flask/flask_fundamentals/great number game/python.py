import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "keep_it_secret_keep_it_safe"


@app.route("/")
def index():
    
    if "number" not in session:
        session["number"] = random.randint(1, 100)
        session["game_status"] = "start"  

    return render_template("index.html")


@app.route("/guess", methods=["POST"])
def guess_number():
    
    user_guess = int(request.form["guess"])

    
    if user_guess == session["number"]:
        session["game_status"] = "win"
    elif user_guess > session["number"]:
        session["game_status"] = "high"
    else:
        session["game_status"] = "low"

    
    return redirect("/")


@app.route("/reset", methods=["POST"])
def reset_game():
    
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)