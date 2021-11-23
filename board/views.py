from django.shortcuts import render, HttpResponse

# Create your views here.
def test(request):
    return HttpResponse("board/test")

def number(request, arg):
    return HttpResponse(arg + ' 페이지 입니다')
