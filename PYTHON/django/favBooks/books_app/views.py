from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Book,User

def books_dashboard(request):
    # Route Guard: Check if user is logged in
    if 'user_id' not in request.session:
        return redirect('/')
        
    current_user = User.objects.get(id=request.session['user_id'])
    
    context = {
        'current_user': current_user,
        'all_books': Book.objects.all(),
        # Retrieve all books favorited by the current user for template checks
        'user_favorites': current_user.liked_books.all()
    }
    return render(request, 'books_app/dashboard.html', context)

def add_book(request):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/books')
            
        current_user = User.objects.get(id=request.session['user_id'])
        
        # Create the book and set who uploaded it
        new_book = Book.objects.create(
            title=request.POST['title'],
            description=request.POST['description'],
            uploaded_by=current_user
        )
        
        # Requirement: Added books should automatically be favorited by the logged-in user
        new_book.users_who_like.add(current_user)
        
    return redirect('/books')

def book_detail(request, book_id):
    if 'user_id' not in request.session:
        return redirect('/')
        
    current_user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    
    context = {
        'current_user': current_user,
        'book': book,
        # List of all users who like this book
        'users_liking': book.users_who_like.all()
    }
    return render(request, 'books_app/book_detail.html', context)

def update_book(request, book_id):
    if request.method == "POST":
        errors = Book.objects.book_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect(f'/books/{book_id}')
            
        book = Book.objects.get(id=book_id)
        # Verify if current user is the uploader before updating
        if book.uploaded_by.id == request.session['user_id']:
            book.title = request.POST['title']
            book.description = request.POST['description']
            book.save()
            
    return redirect(f'/books/{book_id}')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    # Verify if current user is the uploader before deleting
    if book.uploaded_by.id == request.session['user_id']:
        book.delete()
    return redirect('/books')

def toggle_favorite(request, book_id):
    current_user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    
    # Check if action is add or remove based on URL or request
    # If user already likes it, remove them (un-favorite), otherwise add them
    if current_user in book.users_who_like.all():
        book.users_who_like.remove(current_user)
    else:
        book.users_who_like.add(current_user)
        
    # Redirect back to wherever the user clicked it from (dashboard or details page)
    return redirect(request.META.get('HTTP_REFERER', '/books'))