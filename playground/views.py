from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def calculate():
    x = 7
    y = 7
    return x


def say_hello(request):
    x = calculate()
    her = "mkf;sf"
    return render(request, 'hello.html', {'name': 'Happy'})
