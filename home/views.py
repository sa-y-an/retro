from django.shortcuts import render


def home(request) :
    return render(request, 'home/home.html')

def eda(request) :
    return render(request, 'home/eda.html')

def emg(request) :
    return render(request, 'home/emg.html')

def ecg(request) :
    return render(request, 'home/ecg.html')