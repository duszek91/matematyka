from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def add(request, number1, number2):
    return HttpResponse(int(number1) + int(number2))


def sub(request, number1, number2):
    return HttpResponse(int(number1) - int(number2))


def div(request, number1, number2):
    if number2 == "0":
        return HttpResponse("nie dziel przez 0")
    return HttpResponse(int(number1) / int(number2))


def mul(request, number1, number2):
    return HttpResponse(int(number1) * int(number2))