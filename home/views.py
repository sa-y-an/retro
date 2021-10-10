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

        print(path)

        print('here .....................')

        print(ac_class, confidence_score)


        return render(request, 'home/eda.html',{ "class" : ac_class, "score" : confidence_score  } )

    else :
        return render(request, 'home/eda.html')




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
    if request.method == 'POST' :
        path = request.FILES['myfile'] # this is my file
        ac_class, confidence_score = nn_predictions(path,'ECG')

        print(path)

        print('here .....................')

        print(ac_class, confidence_score)


        return render(request, 'home/ecg.html',{ "class" : ac_class, "score" : confidence_score  } )

    else :
        return render(request, 'home/ecg.html')



def resp(request) :
    if request.method == 'POST' :
        path = request.FILES['myfile'] # this is my file
        ac_class, confidence_score = nn_predictions(path,'Resp')

        print(path)

        print('here .....................')

        print(ac_class, confidence_score)


        return render(request, 'home/resp.html',{ "class" : ac_class, "score" : confidence_score  } )

    else :
        return render(request, 'home/resp.html')

def temp(request) :
    if request.method == 'POST' :
        path = request.FILES['myfile'] # this is my file
        ac_class, confidence_score = nn_predictions(path,'Temp')

        print(path)

        print('here .....................')

        print(ac_class, confidence_score)


        return render(request, 'home/temp.html',{ "class" : ac_class, "score" : confidence_score  } )

    else :
        return render(request, 'home/temp.html')

