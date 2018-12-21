# coding:utf-8
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import User


# Create your views here.
def login(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        remember_me = request.POST.get('remember_me')  # ON None
        # user = get_object_or_404(User, name=user_name)
        user = User.objects.get(name=user_name)
        if user is None:
            raise User.DoesNotExist()
        else:
            return render(request, 'mpa/home.html')
    else:
        return render(request, 'mpa/login.html')


def register(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = User()
        user.name = user_name
        User.objects.create()
    else:
        return render(request, 'mpa/register.html')


def reset_pw(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        user = User.objects.get(name=user_name)
        if user is None:
            raise User.DoesNotExist()
        else:
            pass
    else:
        return render(request, 'mpa/recoverpw.html')


def index(request):
    # return response.HttpResponse(u'次茶杯差别万磁王')
    return render(request, 'mpa/index.html')


def home(request):
    return render(request, 'mpa/home.html')


def demos(request, a, b):
    url = 'mpa/demo/' + a + '/' + b + '.html'
    return render(request, url)
