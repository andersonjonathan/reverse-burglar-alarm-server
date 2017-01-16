from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from .models import Message

@login_required
def landing(request):

    return render(request, 'alarm/landing.html', {"content": Message.objects.all()})


@csrf_exempt
def add(request):
    if request.method == "POST":
        if str(request.POST.get('password')) == str(os.environ.get('SECRET_PASSWORD')):
            time = request.POST.get('time')
            m_type = request.POST.get('type')
            message = request.POST.get('message')
            Message.objects.create(time=time, type=m_type, message=message)
            return JsonResponse({"status": "OK"})
    raise Http404
