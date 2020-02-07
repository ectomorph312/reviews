from django.shortcuts import render
from django.http import HttpResponse


def test_login(request):
    return HttpResponse('<h1> Hello world </h1>')