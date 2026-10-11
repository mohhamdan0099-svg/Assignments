import random
from flask import Flask, redirect, render_template, request, session

app = Flask(__name__)
app.secret_key = "ninja_gold_secret"


@app.route("/")
def index():
    
    if "gold" not in session:
        session["gold"] = 0
    if "activities" not in session:
        session["activities"] = []

    return render_template("index.html")


@app.route("/process_money", methods=["POST"])
def process_money():
    building = request.form["building"]
    gold_earned = 0

    
    if building == "farm":
        gold_earned = random.randint(10, 20)
    elif building == "cave":
        gold_earned = random.randint(5, 10)
    elif building == "house":
        gold_earned = random.randint(2, 5)
    elif building == "casino":
        gold_earned = random.randint(-50, 50)

    
    session["gold"] += gold_earned

    
    if gold_earned >= 0:
        message = f"Earned {gold_earned} golds from the {building}!"
        status = "win"
    else:
        message = (
            f"Entered a casino and lost {abs(gold_earned)} golds."
        )
        status = "loss"


    session["activities"].insert(0, {"message": message, "status": status})

    return redirect("/")


@app.route("/reset")
def reset():
    session.clear()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)