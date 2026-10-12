from django.shortcuts import render, redirect, HttpResponse


def register(request):
    return HttpResponse("placeholder for users to create a new user record")

def login(request):
    return HttpResponse("placeholder for users to login.")


def users(request):
    return HttpResponse("placeholder to display all the list of the users later.")