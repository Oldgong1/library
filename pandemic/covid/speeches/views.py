from django.shortcuts import render
from .models import Speech, Speaker
from django.http import HttpResponse

# Create your views here.

    
def index(request):
    return render(request, "speeches/index.html")
       
def speech(request):
    context = {
        "speak" : Speech.objects.all()
    } 
    return render(request, "Speeches/speech.html", context)      

def speaker(request):
    context = {
        "speaker" : Speaker.objects.all()
    }
    return render(request, "Speeches/speaker.html", context) 
  



