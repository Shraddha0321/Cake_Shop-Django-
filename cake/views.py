from django.shortcuts import render
from django.http import HttpResponse
from .models import Cake
# Create your views here.

def home(request):
    cake = Cake.objects.all()
    return render(request, 'home.html', {'cake': cake})