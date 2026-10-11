from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse

# 1. Root route: redirects to "/blogs"
def root(request):
    return redirect('/blogs')

# 2. Index route: displays string placeholder
def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

# 3. New route: displays form placeholder
def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

# 4. Create route: redirects to "/"
def create(request):
    return redirect('/')

# 5. Show route: displays specific blog number using route parameter
def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")

# 6. Edit route: displays edit message for specific blog number
def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")

# 7. Destroy route: redirects to "/blogs"
def destroy(request, number):
    return redirect('/blogs')

# 8. Bonus route: returns JsonResponse with title and content
def json_response(request):
    return JsonResponse({
        "title": "My first blog",
        "content": "Lorem, ipsum dolor sit amet consectetur adipisicing elit."
    })
