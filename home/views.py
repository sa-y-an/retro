from django.shortcuts import render


def home(request) :
    return render(request, 'home/home.html')

def eda(request) :
    return render(request, 'home/eda.html')

def emg(request) :
    return render(request, 'home/emg.html')

def ecg(request) :
    return render(request, 'home/ecg.html')

def resp(request) :
    return render(request, 'home/resp.html')

def temp(request) :
    return render(request, 'home/temp.html')


def about(request) :
    return render(request, 'home/about.html')