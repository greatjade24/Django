from django.shortcuts import HttpResponse as hr


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