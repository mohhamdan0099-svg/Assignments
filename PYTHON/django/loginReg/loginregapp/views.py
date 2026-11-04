from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User

def index(request):
    return render(request, 'index.html')

def register(request):
    if request.method == "POST":
        # 1. Run validator checks
        errors = User.objects.register_validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/')
            
        # 2. Hash the password
        password = request.POST['password']
        hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
        
        # 3. Create user in database with the hashed password
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_password
        )
        
        # 4. Save user ID in session to log them in
        request.session['user_id'] = new_user.id
        return redirect('/success')
        
    return redirect('/')

def login(request):
    if request.method == "POST":
        # 1. Find user by email input
        user_list = User.objects.filter(email=request.POST['email'])
        
        if user_list:
            logged_user = user_list[0]
            
            # 2. Check if entered password matches the stored hash
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                # 3. Save user ID in session
                request.session['user_id'] = logged_user.id
                return redirect('/success')
                
        # If login fails
        messages.error(request, "Invalid Email/Password")
    return redirect('/')

def success(request):
    # Route guard: check if user is logged in
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'success.html', context)

def logout(request):
    # Clear session
    request.session.clear()
    return redirect('/')