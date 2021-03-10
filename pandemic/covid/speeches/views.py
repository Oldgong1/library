from django.shortcuts import render
from .models import Speech, Speaker
from django.http import HttpResponse
from django.views import generic

# Create your views here.

def index(request):
    num_speeches = Speech.objects.all().count()
    num_speakers = Speaker.objects.count()
    context = {
        'num_speeches': num_speeches,
        'num_speakers': num_speakers,
    }
    return render(request, "Speeches/index.html", context=context)    
    
        
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
  



