from django.shortcuts import render

# Create your views here.
#session 
def setsession(request):
    request.session['name']='ankit'
    return render(request,'myapp/setsession.html')
def getsession(request):
    name=request.session['name']
    return render(request,'myapp/getsession.html',{'name':name})


def deletesession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'myapp/deletesession.html')
