from django.shortcuts import render, redirect
from .models import User

def index(request):
    context = {
        
        "all_the_users": User.objects.all()
    }
    return render(request, "index.html", context)

def create_user(request):
    if request.method == "POST":
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email_address=request.POST['email'],
            age=request.POST['age']
        )
    return redirect('/')


def delete(request,id):
    
    delete_user = User.objects.get(id=id)
    delete_user.delete()
        
    return redirect('/',) 


    
