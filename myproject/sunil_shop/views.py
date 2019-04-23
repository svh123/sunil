from django.shortcuts import render

# Create your views here.


def home_page(request):

    return render(request, "dummy.html")


def home_page1(request):

    return render(request, "sunil_shop_home.html")
