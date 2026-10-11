from django.shortcuts import render, redirect, HttpResponse
from django.http import JsonResponse


def root(request):
    return redirect('/blogs')


def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")


def new(request):
    return render(request,"index.html")


def create(request):
    return redirect('/')


def show(request, number):
    return HttpResponse(f"placeholder to display blog number: {number}")


def edit(request, number):
    return HttpResponse(f"placeholder to edit blog {number}")


def destroy(request, number):
    return redirect('/blogs')

