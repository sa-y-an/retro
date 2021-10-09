from django.http.response import HttpResponse
from django.shortcuts import render
from .classifier import nn_predictions


def home(request) :
    return render(request, 'home/home.html')


def about(request) :
    return render(request, 'home/about.html')


# modalities

def eda(request):
    if request.method == 'POST' :
        path = request.FILES['myfile'] # this is my file
        ac_class, confidence_score = nn_predictions(path,'EDA')

        print(ac_class, confidence_score)


        return render(request, 'home/emg.html',{ "class" : ac_class, "score" : confidence_score, "path" :path  } )

    else :
        return render(request, 'home/emg.html')
    




def emg(request) :

    if request.method == 'POST' :
        path = request.FILES['myfile'] # this is my file
        ac_class, confidence_score = nn_predictions(path,'EMG')

        print(path)

        print('here .....................')

        print(ac_class, confidence_score)


        return render(request, 'home/emg.html',{ "class" : ac_class, "score" : confidence_score  } )

    else :
        return render(request, 'home/emg.html')



def ecg(request) :
    return render(request, 'home/ecg.html')

def resp(request) :
    return render(request, 'home/resp.html')

def temp(request) :
    return render(request, 'home/temp.html')

