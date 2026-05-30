from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("👋 Главная страница каталога работает!")

def contacts(request):
    return render(request, 'contacts.html')