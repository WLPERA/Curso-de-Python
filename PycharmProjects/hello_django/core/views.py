from django.shortcuts import render, HttpResponse

def hello(request,nome,idade):
    return HttpResponse('<h1>Hello {} de {} anos</h1>'.format(nome,idade))

# Create your views here.
