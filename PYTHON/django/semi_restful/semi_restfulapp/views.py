from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Show


def start(request):

    return redirect('/shows')


def all_shows(request):

    context={"all_shows":Show.objects.all()
                                }
    return render(request,"all_shows.html",context)


def index(request):

    return render(request,"index.html")


def create(request):
    if request.method== "POST":
        errors = Show.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)

            request.session['temp_title'] = request.POST['title']
            request.session['temp_net'] = request.POST['network']   
            request.session['temp_desc'] = request.POST['desc']
            return redirect('/shows/new/')
        else:
            show=Show.objects.create(
                title=request.POST['title'],
                network=request.POST['network'],
                release_date=request.POST['date'],
                description=request.POST['desc'],
                )
    return redirect(f'/shows/{show.id}')

def new_show(request,id):
    show=Show.objects.get(id=id)
    context={
        "show":show
    }
    return render(request,"show.html",context)


def delete(request,id):

    deleted_show=Show.objects.get(id=id)
    deleted_show.delete()
    return redirect('/shows')


def edit(request,id):

    show=Show.objects.get(id=id)
    context={
        "show":show,
        
    }
    return render(request,"edit.html",context)

def update(request,id):

    if request.method== "POST":
        errors = Show.objects.validator(request.POST)
        if errors:
            for key, value in errors.items():
                messages.error(request, value)
    
                request.session['temp_title'] = request.POST['title']
                request.session['temp_net'] = request.POST['network']   
                request.session['temp_desc'] = request.POST['desc']
            return redirect(f"/shows/edit/{id}/")
        else:
            edited=Show.objects.get(id=id)
            edited.title=request.POST['title']
            edited.network=request.POST['network']
            edited.release_date=request.POST['date']
            edited.description=request.POST['desc']
            edited.save()
            return redirect(f"/shows/{id}/")
    
    
    
    




