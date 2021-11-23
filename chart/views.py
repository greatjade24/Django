from django.shortcuts import render, HttpResponse

# Create your views here.
def year(request, arg):
    return HttpResponse(arg + "년도 페이지")

def month(request, arg):
    return HttpResponse(arg + "월 페이지")