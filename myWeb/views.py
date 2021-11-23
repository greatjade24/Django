from django.shortcuts import HttpResponse as hr
from django.shortcuts import render


def test(request):
    return hr("test")


def index(request):
    return hr("Index Page")


def notice(request):
    return hr("Notice Page")


def board(request, boardId):
    print(type(boardId))
    message = f'{boardId} page'
    return hr(message)


def language(request, languageId):
    if languageId == 'en':
        return hr("영어")
    elif languageId == 'ko':
        return hr("한국어")
    elif languageId == 'jp':
        return hr("일본어")
    else:
        return hr("알 수 없는 언어")

    # lang_code = {'ko' : '한국어', 'en' : '영어', 'jp' : '일본어'}

    # if lang_code.get(languageId):
    #   message = f'{lang_code.get(languageId)}'
    # else:
    #   message = '알 수 없는 언어'
    # return hr(message);


def reg1(request, arg):
    return hr(arg)


def reg2(request, arg):
    return hr(arg)


def reg3(request, arg):
    return hr(arg)


def reg4(request, arg):
    return hr(arg)


def reg5(request, arg):
    return hr(arg)


def reg6(request, arg):
    return hr(arg)


def reg7(request, arg):
    print(type(arg))
    return hr(arg)


def reg8(request, arg):
    print(type(arg))
    return hr(arg)


def reg9(request, arg):
    return hr(arg)


def reg10(request, arg):
    return hr(arg)


def reg11(request, arg):
    return hr(arg)


def reg12(request, arg):
    return hr(arg)


def reg13(request, arg):
    return hr(arg)


def reg14(request, arg):
    return hr(arg)


def reg15(request, arg):
    return hr(arg)


def reg16(request, arg):
    return hr(arg)


def email(request, arg):
    return hr(arg)


def lang(request, arg):
    return hr(arg)


def temp1(request):
    return render(request, 'temp1.html')


def temp2(request):
    context = {
        "key": "value",
        "num": 100,
        "float": 1.234,
        "String": "문자열",
        "list": [10, 20, '리스트'],
        "dic": {"a": "a값", "b": "b값"},
    }
    return render(request, 'temp2.html', context)


def temp3(request):
    context = {
        "list": [10, 20, '리스트'],
        "dic": {"a": "a값", "b": "b값"},
    }
    return render(request, 'temp3.html', context)


def quiz01(request):
    context = {
        "seq": [[1, 2, 3, 4, 5], ['육', 7, '팔', '구', 10], [11, 12, 13, 14, 15]],
    }
    return render(request, 'quiz/quiz01.html', context)


def quiz02(request):
    context = {
        "dic": {'네이버': 'https://www.naver.com', '구글': 'https://www.google.com', '다음': 'https://www.daum.net'}
    }
    return render(request, 'quiz/quiz02.html', context)


def quiz03(request):
    context = {
        "menu":['순위','국가','승점','승','무','패','득점','실점','골득실'],
        "score": [
            [1, {"이란": "https://overseas.mofa.go.kr/ir-ko/index.do"}, 17, 5, 2, 0, 6, 0, 6],
            [2, {"대한민국": "http://www.president.go.kr/"}, 13, 4, 1, 2, 9, 7, 2],
            [3, {"시리아": "https://www.0404.go.kr/dev/country_view.mofa?idx=131"}, 8, 2, 2, 3, 2, 3, -1],
        ],
    }
    return render(request, 'quiz/quiz03.html', context)

def image(request):
    return render(request, 'image.html')
