from django.shortcuts import render, redirect
from .models import Member
# Create your views here.

def index(request):
    mem = Member.objects.all()
    return render(request, 'index.html', {"mem":mem})

def add(request):
    return render(request, 'add.html')

def adres(request):
    a = request.POST['first_name']
    b = request.POST['last_name']
    c = request.POST['email']
    d = request.POST['birthdate']
    e = request.POST['gender']

    mem = Member(first_name = a, last_name = b, email = c, birthdate = d, gender = e)
    mem.save()

    # return redirect("/")
    return index(request)

def delete(request, id):
    mem = Member.objects.get(id = id)
    mem.delete()
    # return redirect("/")
    return index(request)



def update(request, id):
    mem = Member.objects.get(id = id)
    return render(request, 'update.html', {"mem":mem})

def upres(request, id):
    mem = Member.objects.get(id = id)
    a = request.POST['first_name']
    b = request.POST['last_name']
    c = request.POST['email']
    d = request.POST['birthdate']
    e = request.POST['gender']

    mem.first_name = a
    mem.last_name = b
    mem.email = c
    mem.birthdate =d
    mem.gender = e

    mem.save()
    # return redirect("/")
    return index(request)

