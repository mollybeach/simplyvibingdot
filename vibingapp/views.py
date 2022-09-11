#from pyrebase import pyrebase
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def donate(request):
    return render(request, 'donate.html')


config = {
    "apiKey": "AIzaSyAfDmTJ7kn-ox_8FqLOozeusG1JrzxjlYY",
    "authDomain": "simplyvibingdotcom-cd8b1.firebaseapp.com",
    "projectId": "simplyvibingdotcom-cd8b1",
    "storageBucket": "simplyvibingdotcom-cd8b1.appspot.com",
    "messagingSenderId": "397746192879",
    "appId": "1:397746192879:web:efce8257d48d5f6b18361a",
    "measurementId": "G-CCQN9FGD1P"
}  

#firebase = pyrebase.initialize_app(config)
#auth = firebase.auth()
