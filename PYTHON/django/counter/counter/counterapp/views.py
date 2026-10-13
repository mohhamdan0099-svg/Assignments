from django.shortcuts import render,redirect

def index(request):

    if "count" not in request.session:
        request.session['count']=1
    else:
        request.session['count']+=1    


    return render(request,"index.html")


def destroy(request):
    
    del request.session['count']
    return redirect('/')