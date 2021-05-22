from django.urls import path

from . import views

urlpatterns = [
    path('<number1>/<number2>/', views.add),
    path('<number1>/<number2>/', views.sub),
    path('<number1>/<number2>/', views.div),
    path('<number1>/<number2>/', views.mul),
]