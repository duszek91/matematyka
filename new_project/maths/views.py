from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def add(request, number1, number2):
    return HttpResponse(f"{number1 + number2}")


def sub(request, number1, number2):
    return HttpResponse(f"{number1 - number2}")


def div(request, number1, number2):
    return HttpResponse(f"{number1 / number2}")


def mul(request, number1, number2):
    return HttpResponse(f"{number1 * number2}")