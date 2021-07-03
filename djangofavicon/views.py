from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import render


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, 'home.html')
