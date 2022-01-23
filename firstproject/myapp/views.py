from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse('helloworld')


def zifuchuan(request):
    str1 = "DjAnG0_1S_Very_iNt3resT1n"
    return render(request,"test.html",{"name":str1})
import random

def num3(request):
    num_list = []
    for i in range(1,101):
        if i % 2 == 0:
            num_list.append(i)
    a = random.randint(0,101)
    return render(request,"test2.html",{"numlist":num_list,"num":a})

def index1(request):
    return render(request,"index.html")

