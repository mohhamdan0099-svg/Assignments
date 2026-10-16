from django.shortcuts import render, redirect
from .models import Dojo,Ninja

def index(request):
    context = {
        
        "all_the_dojos": Dojo.objects.all() ,
                
    }

    return render(request, "index.html", context)

def create_dojo(request):
    if request.method == "POST":
        Dojo.objects.create(
            name=request.POST['name'],
            city=request.POST['city'],
            state=request.POST['state'],
        )

        
    return redirect('/')


def create_ninja(request):
    if request.method == "POST":
        selected_dojo = Dojo.objects.get(id=request.POST['dojo_id'])
        Ninja.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            dojo=selected_dojo
        )

    return redirect('/')


def delete(request,id):

    if request.method == "POST":

        delete_dojo = Dojo.objects.get(id=id)
        delete_dojo.delete()

    return redirect('/')