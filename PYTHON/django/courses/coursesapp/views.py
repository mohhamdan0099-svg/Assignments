from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Course

def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "index.html", context)

def create_course(request):
    if request.method == "POST":
        errors = Course.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
            
            request.session['temp_name'] = request.POST['name']
            request.session['temp_desc'] = request.POST['description']
            return redirect('/')
        else:        
            Course.objects.create(
                name=request.POST['name'],
                description=request.POST['description']
            )
            for key in ['temp_name', 'temp_desc']:
                request.session.pop(key, None)
                    
    return redirect('/')

def destroy_page(request, id):
    context = {
        "course": Course.objects.get(id=id)
    }
    return render(request, "destroy.html", context)

def destroy(request, id):
    if request.method == "POST":
        course = Course.objects.get(id=id)
        course.delete()
    return redirect('/')