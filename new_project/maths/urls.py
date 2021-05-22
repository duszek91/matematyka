from django.urls import path

from . import views

urlpatterns = [
    path('add/<number1>/<number2>/', views.add),
    path('sub/<number1>/<number2>/', views.sub),
    path('div/<number1>/<number2>/', views.div),
    path('mul/<number1>/<number2>/', views.mul),
]