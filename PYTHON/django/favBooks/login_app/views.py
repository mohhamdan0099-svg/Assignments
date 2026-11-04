from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
            
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_password
        )
        request.session['user_id'] = new_user.id
        return redirect('/books')
        
    return redirect('/')

def login(request):
    if request.method == "POST":
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            logged_user = user_list[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/books')
                
        messages.error(request, "Invalid Email/Password")
    return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')