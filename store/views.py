from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory

from django.contrib.auth import authenticate, login, logout
import requests
from django.contrib.auth import login as auth_login

from django.contrib import messages

from django.contrib.auth.decorators import login_required

# Create your views here.

from .forms import  CreateUserForm

def store(request):
    context = {}
    return render(request, 'store/store.html', context)

def traingrid(request):
    context = {}
    return render(request, 'store/traingrid.html', context)

def checkout(request):
    context = {}
    return render(request, 'store/checkout.html', context)
      
def register(request):

    # This part runs if some post request is done.
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        # Checking if the form is valid or not.
        if form.is_valid():

            # If the form is valid, then we are saving the form and redirecting user to home page.
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            messages.success(request, 'Account was created for '+ username)
            
            return redirect(store)
    else:
        form = CreateUserForm()
    
    context = {'form': form}
    return render(request, 'regestration/register.html', context)
    
def login(request):
    
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(username = username, password = password)
        if user is not None:
            auth_login(request, user)
            return redirect('store')
        else:
            messages.info(request, 'Username OR password is incorrect')      
    context = {}
    return render(request, 'regestration/login.html', context)

def main(request):
    context= {}
    return render(request,'store/main.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')




# Import libraray

# Create this function as it is in views.py file.
# Keyword can be train id or name.
def getData(keyword):
    url = "https://trains.p.rapidapi.com/"

    payload = "{\r\"search\": \""+keyword+"\"\r}"
    headers = {
        'content-type': "application/json",
        'x-rapidapi-key': "4615bcee91msh3c01d8a800e1a46p1c4d3cjsna6d3ac46edda",
        'x-rapidapi-host': "trains.p.rapidapi.com"
        }

    response = requests.request("POST", url, data=payload, headers=headers)

    return response.json()
'''
# Calling the function.
# Here, I have tested function with train id you can pass name also.
result = getData("12168")


# Processing Data for HTML side.
data = []

for train in result:
    train_id = train['train_num']
    name = train['name']
    source = train['train_from']
    destination = train['train_to']
    traindata = train['data']['days']
    days = []
    for key, value in traindata.items():
        if value == 1:
            days.append(key)
    classes = train['data']['classes']
    departtime = train['data']['departTime']
    arriveTime = train['data']['arriveTime']

    data.append({
        'train_num': train_id,
        'name': name,
        'source': source,
        'destination': destination,
        'classes': classes,
        'departtime': departtime,
        'arrivetime': arriveTime,
        'days': days
        })

# Single values, call directly on html side.
print(train_id, name, source, destination, departtime, arriveTime)

# Multiple values, use for loop when calling on html side.
print(days)
print(classes)
print(data)


    
# return this with request.
context = {
    'data': data
    }
'''
def train(request):
    
    value = ""
    if request.method == "POST":
        value = request.POST["search"]
        
    result = getData(value)
    data = []

    for train in result:
        train_id = train['train_num']
        name = train['name']
        source = train['train_from']
        destination = train['train_to']
        traindata = train['data']['days']
        days = []
        for key, value in traindata.items():
            if value == 1:
                days.append(key)
        classes = train['data']['classes']
        departtime = train['data']['departTime']
        arriveTime = train['data']['arriveTime']

        data.append({
            'train_num': train_id,
            'name': name,
            'source': source,
            'destination': destination,
            'classes': classes,
            'departtime': departtime,
            'arrivetime': arriveTime,
            'days': days
        })
    context = {
        'data': data
    }
    print(context)
    return render(request,'store/traingrid.html',context)
