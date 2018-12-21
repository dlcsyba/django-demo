# coding:utf-8
from django.http import response
from django.shortcuts import render

# Create your views here.
def index(request):
    #return response.HttpResponse(u'次茶杯差别万磁王')
    return render(request, 'learn/home.html')

def add(request):
    a = request.GET.get('a', 0)
    b = request.GET.get('b', 0)
    c = int(a) + int(b)
    return response.HttpResponse(c)

def add2(request, a=0, b=0):
    c = int(a) + int(b)
    return response.HttpResponse(c)

#def old_add2_redirect(request, a, b):
#    response.HttpResponseRedirect()