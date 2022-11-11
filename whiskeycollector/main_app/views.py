from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from .models import Whiskey, WhiskeyTypes, TYPES

class WhiskeyCreate(CreateView):
    model = Whiskey
    fields = '__all__'

class WhiskeyUpdate(UpdateView):
    model = Whiskey
    fields = '__all__'

class WhiskeyDelete(DeleteView):
    model = Whiskey
    success_url = '/whiskey/'

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def whiskey_index(request):
    whiskeys = Whiskey.objects.all()
    types = WhiskeyTypes.objects.all()
    return render(request, 'main_app/index.html', { 'whiskeys': whiskeys, 'types': types })

def whiskey_detail(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    type = WhiskeyTypes.objects.get(id=whiskey.type_id)
    return render(request, 'main_app/detail.html', { 'whiskey': whiskey, 'type': type })

def whiskey_create(request):
    types = TYPES
    return render(request, 'main_app/create.html', { 'types': types})

# Need to add Whiskey Types to database
def whiskey_add(request):
    data = request.POST
    name = data["name"]
    whiskeyType = WhiskeyTypes.objects.get(type=data["type"])
    type_id = whiskeyType.id
    origin = data["origin"]
    subType = data["subType"]
    price = data["price"]
    volume = data["volume"]
    description = data["description"]
    w = Whiskey(name=name, type_id=type_id, origin=origin, subType=subType, price=price, volume=volume, description=description)
    w.save()
    return redirect('index')

def whiskey_edit(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    types = TYPES
    currentType = WhiskeyTypes.objects.get(id=whiskey.type_id)
    return render(request, 'main_app/edit.html', { 'whiskey': whiskey, 'currentType': currentType, 'types': types })

def whiskey_update(request, whiskey_id):
    whiskey = Whiskey.objects.get(id=whiskey_id)
    data = request.POST
    name = data['name']
    whiskeyType = WhiskeyTypes.objects.get(type=data["type"])
    type_id = whiskeyType.id
    origin = data["origin"]
    subType = data["subType"]
    price = data["price"]
    volume = data["volume"]
    description = data["description"]
    w = Whiskey(id=whiskey_id, name=name, type_id=type_id, origin=origin, subType=subType, price=price, volume=volume, description=description)
    w.save()
    return redirect('index')