from django.shortcuts import render, redirect, HttpResponse


def display(request):
    return HttpResponse("placeholder display all the surveys created.")

def new(request):
    return HttpResponse("placeholder for users to add new survey.")