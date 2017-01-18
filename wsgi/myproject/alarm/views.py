from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import os
from .models import Message


@login_required
def landing(request):

    return render(request, 'alarm/landing.html', {"content": Message.objects.filter(type="movement").order_by("-time")[0:10],
                                                  "ping": Message.objects.filter(type="ping").order_by("-time").first()})


@login_required
def clean(request):
    movements = Message.objects.filter(type="movement").order_by("-time")[10:].values_list("id", flat=True)
    Message.objects.filter(pk__in=list(movements)).delete()
    pings = Message.objects.filter(type="ping").order_by("-time")[2:].values_list("id", flat=True)
    Message.objects.filter(pk__in=list(pings)).delete()
    return render(request, 'alarm/landing.html',
                  {"content": Message.objects.filter(type="movement").order_by("-time")[0:10],
                   "ping": Message.objects.filter(type="ping").order_by("-time").first()})


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
