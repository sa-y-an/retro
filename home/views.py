from django.shortcuts import render


def home(request) :
    return render(request, 'home/home.html')

def eda(request) :
    return render(request, 'home/eda.html')