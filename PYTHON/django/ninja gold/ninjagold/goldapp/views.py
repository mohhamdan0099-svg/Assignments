from django.shortcuts import render,redirect
import random

def index(request):
    if "gold" not in request.session:
        request.session["gold"] = 0
    if "activities" not in request.session:
        request.session["activities"] = []

    return render(request,"index.html")


def process_money(request):
    building = request.POST["building"]
    gold_earned = 0

    
    if building == "farm":
        gold_earned = random.randint(10, 20)
    elif building == "cave":
        gold_earned = random.randint(5, 10)
    elif building == "house":
        gold_earned = random.randint(2, 5)
    elif building == "casino":
        gold_earned = random.randint(-50, 50)

    
    request.session["gold"] += gold_earned

    
    if gold_earned >= 0:
        message = f"Earned {gold_earned} golds from the {building}!"
        status = "win"
    else:
        message = (
            f"Entered a casino and lost {abs(gold_earned)} golds."
        )
        status = "loss"


    request.session["activities"].insert(0, {"message": message, "status": status})

    return redirect("/")


def reset(request):
    del request.session["gold"]
    del request.session["activities"]
    return redirect("/")

