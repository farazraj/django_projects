from django.shortcuts import render
from .models import *
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .forms import updaterecordform
from django.contrib import messages

# Create your views here.
def create(request):
    if request.method == "POST":
        crud = Crud()
        crud.name = request.POST.get('name')
        crud.age = request.POST.get('age')
        crud.company = request.POST.get('company')
        crud.location = request.POST.get('locations')
        crud.save()
    loclist = Location.objects.all()
    return render(request, 'create.html',{'loclist':loclist})

def retrieve(request):
    crudlist = Crud.objects.all()
    return render (request, 'retrieve.html',{'crudlist':crudlist})

def location(request):
    if request.method == 'POST':
        location = Location()
        location.loc_id = request.POST.get('loc_id')
        location.loc_name = request.POST.get('loc_name')
        location.save()

    loclist = Location.objects.all()

    return render(request, 'location.html',{'loclist':loclist})

def delete(request, id):
     crud = Crud.objects.get(id=id)
     crud.delete()
     return HttpResponseRedirect( reverse('retrieve'))

def deleteloc(request, loc_id):
     loc = Location.objects.get(loc_id=loc_id)
     loc.delete()
     return HttpResponseRedirect( reverse('location'))


def update(request, id):
    crud = Crud.objects.get(id=id)
    return render(request, 'update.html',{'crud':crud})

def updaterecord(request, id):

    crud = Crud.objects.get(id=id)
    form = updaterecordform(request.POST, instance=crud)
    if form.is_valid:
        form.save()
        messages.success(request,"Record Updated Successfully!!")

    return HttpResponseRedirect( reverse('retrieve'))


# name = request.POST['name']
# age = request.POST['age']
# company = request.POST['company']
# location = request.POST['locations']
#
# crud = Crud.objects.get(id=id)
# crud.name = name
# crud.age = age
# crud.company = company
# crud.locations = location
#
# crud.update()
