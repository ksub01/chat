from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('Никита иди на ***')


def index(request):
    try:
        with open('./nikita.jpeg', "rb") as f:
            return HttpResponse(f.read(), content_type="image/jpeg")
    except IOError:
        return HttpResponse('Ошибка загрузки фото')
