from django.db import models
import re

class UserManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # First name validation
        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name must be at least 2 characters."
        elif not postData['first_name'].isalpha():
            errors["first_name"] = "First name must contain letters only."
            
        # Last name validation
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name must be at least 2 characters."
        elif not postData['last_name'].isalpha():
            errors["last_name"] = "Last name must contain letters only."
            
        # Email validation using Regex
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email address format."
            
        # Password validation
        if len(postData['password']) < 8:
            errors["password"] = "Password must be at least 8 characters."
        if postData['password'] != postData['confirm_password']:
            errors["password_confirm"] = "Passwords must match."
            
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    
    objects = UserManager()