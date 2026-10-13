import random
from django.shortcuts import render,redirect

def index(request):
    if "number" not in request.session:
        request.session["number"]= random.randint(1, 100)
        request.session["status"]="start"
    return render(request,"index.html")


def guess(request):

    user_guess = int(request.POST["guess"])

    
    if user_guess == request.session["number"]:
        request.session["status"] = "win"
    elif user_guess > request.session["number"]:
        request.session["status"] = "high"
    else:
        request.session["status"] = "low"

    return redirect("/")


def reset(request):
    
    del request.session["number"]
    return redirect("/")


