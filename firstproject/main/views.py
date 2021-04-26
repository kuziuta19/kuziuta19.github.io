from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    data = {
        'title': 'Главная страница',
        'values': ['Some', 'Hello', '123'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'Football'
        }
    }
    return render(request, 'main/index.html', data)


def about(request):
    return render(request, 'main/html/index.html')


def page2(request):
    return render(request, 'main/html/page2.html')


def page3(request):
    return render(request, 'main/html/page3.html')
