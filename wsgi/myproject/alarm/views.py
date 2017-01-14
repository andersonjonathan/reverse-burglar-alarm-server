from django.shortcuts import render


def landing(request):

    return render(request, 'alarm/landing.html', {"content": "hej1"})


def add(request):

    return render(request, 'alarm/landing.html', {"content": "hej"})
