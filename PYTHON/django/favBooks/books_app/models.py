from django.db import models
from login_app.models import User

class BookManager(models.Manager):
    def book_validator(self, postData):
        errors = {}
        # Title is required
        if len(postData['title']) < 1:
            errors["title"] = "Title is required."
        # Description must be at least 5 characters
        if len(postData['description']) < 5:
            errors["description"] = "Description must be at least 5 characters long."
        return errors

class Book(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    
    # One-to-Many: User who uploaded the book
    uploaded_by = models.ForeignKey(User, related_name="books_uploaded", on_delete=models.CASCADE)
    
    # Many-to-Many: Users who have favorited/liked the book
    users_who_like = models.ManyToManyField(User, related_name="liked_books")
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    objects = BookManager()