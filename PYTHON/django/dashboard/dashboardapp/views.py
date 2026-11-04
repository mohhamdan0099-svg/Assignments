from django.shortcuts import render, redirect
from django.contrib import messages
import bcrypt
from .models import User, Message

# 1. Landing & Authentication Views

def index(request):
    """Landing page / Welcome page"""
    return render(request, 'user_dashboard/index.html')

def signin_page(request):
    """Render the Login page"""
    return render(request, 'user_dashboard/signin.html')

def register_page(request):
    """Render the Registration page"""
    return render(request, 'user_dashboard/register.html')

def register_process(request):
    """Process registration form and hash password"""
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/register/')
            
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        # Make the very first registered user an Admin (Level 9), others Normal (Level 1)
        user_count = User.objects.count()
        assigned_level = 9 if user_count == 0 else 1
        
        new_user = User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_password,
            user_level=assigned_level
        )
        
        request.session['user_id'] = new_user.id
        return redirect('/dashboard/')
    return redirect('/')

def login_process(request):
    """Process login and check password hash"""
    if request.method == "POST":
        user_list = User.objects.filter(email=request.POST['email'])
        if user_list:
            logged_user = user_list[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.password.encode()):
                request.session['user_id'] = logged_user.id
                return redirect('/dashboard/')
                
        messages.error(request, "Invalid Email or Password.")
        return redirect('/signin/')
    return redirect('/')

def logout(request):
    """Clear session and log out"""
    request.session.clear()
    return redirect('/')


# 2. Dashboard View (Handles both Admin and Normal layouts)

def dashboard(request):
    """Main dashboard showing users table depending on privilege level"""
    if 'user_id' not in request.session:
        return redirect('/')
        
    current_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'current_user': current_user,
        'all_users': User.objects.all()
    }
    return render(request, 'user_dashboard/dashboard.html', context)


# 3. Admin User Management Views

def new_user_page(request):
    """Admin page to manually add a new user"""
    if 'user_id' not in request.session:
        return redirect('/')
    current_user = User.objects.get(id=request.session['user_id'])
    if current_user.user_level != 9:
        return redirect('/dashboard/')
        
    return render(request, 'user_dashboard/new_user.html')

def create_user_process(request):
    """Process admin manual user creation"""
    if request.method == "POST":
        errors = User.objects.register_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/users/new/')
            
        hashed_password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
        
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=hashed_password,
            user_level=int(request.POST.get('user_level', 1))
        )
    return redirect('/dashboard/')

def delete_user(request, user_id):
    """Admin removing a user from the system"""
    if 'user_id' not in request.session:
        return redirect('/')
    current_user = User.objects.get(id=request.session['user_id'])
    
    if current_user.user_level == 9:
        user_to_delete = User.objects.get(id=user_id)
        user_to_delete.delete()
        
    return redirect('/dashboard/')

def admin_edit_user_page(request, user_id):
    """Admin page to edit another user's info & level"""
    if 'user_id' not in request.session:
        return redirect('/')
    current_user = User.objects.get(id=request.session['user_id'])
    if current_user.user_level != 9:
        return redirect('/dashboard/')
        
    context = {
        'target_user': User.objects.get(id=user_id)
    }
    return render(request, 'user_dashboard/admin_edit_user.html', context)


# 4. Profile & Update Views (Self or Admin updates)

def edit_profile_page(request):
    """User editing their own profile details and password"""
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'current_user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'user_dashboard/edit_profile.html', context)

def update_user_process(request, user_id):
    """Process updates to profile data, description, or password"""
    if request.method == "POST":
        user_to_update = User.objects.get(id=user_id)
        
        # Check if updating profile info vs password
        if 'first_name' in request.POST:
            user_to_update.first_name = request.POST['first_name']
            user_to_update.last_name = request.POST['last_name']
            user_to_update.email = request.POST['email']
            
            # If admin is updating user level, save it too
            if 'user_level' in request.POST:
                user_to_update.user_level = int(request.POST['user_level'])
                
            user_to_update.save()
            
        elif 'description' in request.POST:
            user_to_update.description = request.POST['description']
            user_to_update.save()
            
        elif 'password' in request.POST:
            if request.POST['password'] == request.POST['password_confirm'] and len(request.POST['password']) >= 8:
                user_to_update.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt()).decode()
                user_to_update.save()
            else:
                messages.error(request, "Passwords must match and be at least 8 characters.")
                
    return redirect('/dashboard/')


# 5. User Wall & Messages Views

def user_profile(request, user_id):
    """Show specific user's wall messages and details"""
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'profile_user': User.objects.get(id=user_id),
    }
    return render(request, 'user_dashboard/user_profile.html', context)

def post_message(request, user_id):
    """Post a wall message on a user's profile page"""
    if request.method == "POST" and 'user_id' in request.session:
        poster_user = User.objects.get(id=request.session['user_id'])
        wall_owner = User.objects.get(id=user_id)
        
        if len(request.POST['content']) > 0:
            Message.objects.create(
                content=request.POST['content'],
                poster=poster_user,
                wall_user=wall_owner
            )
            
    return redirect(f'/users/show/{user_id}')