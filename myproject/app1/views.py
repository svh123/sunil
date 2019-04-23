from django.shortcuts import render
from .forms import *
# Create your views here.



def first(request):
    #file = ["Shiva","Kumar","VH"]
    file = user_reg()
    return render(request,"test.html",{'data':file})
