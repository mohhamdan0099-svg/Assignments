from django.shortcuts import render, redirect
from django.contrib import messages
from loginapp.models import User
from .models import Message, Comment

def wall(request):
    # Route guard: block access if user is not in session
    if 'user_id' not in request.session:
        return redirect('/')
        
    context = {
        'current_user': User.objects.get(id=request.session['user_id']),
        'all_messages': Message.objects.all().order_by("-created_at")
    }
    return render(request, 'wall.html', context)

def post_message(request):
    if request.method == "POST":
        if len(request.POST['message']) < 1:
            messages.error(request, "Message cannot be blank.")
        else:
            user = User.objects.get(id=request.session['user_id'])
            Message.objects.create(message=request.POST['message'], user=user)
    return redirect('/wall')

def post_comment(request, message_id):
    if request.method == "POST":
        if len(request.POST['comment']) < 1:
            messages.error(request, "Comment cannot be blank.")
        else:
            user = User.objects.get(id=request.session['user_id'])
            message = Message.objects.get(id=message_id)
            Comment.objects.create(comment=request.POST['comment'], user=user, message=message)
    return redirect('/wall')