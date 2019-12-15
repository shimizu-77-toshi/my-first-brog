from django.http.response import HttpResponse
from django.shortcuts import render
# ウェブサイトにきた人に送り返すための内容

def hello_world(request):
    return HttpResponse('HelloWorld')
# HTTPレスポンス( サーバーからの返信 )を返している。
# webリクエストを引数にとり、webレスポンスを返す関数

def hello_template(request):
    return render(request, 'index.html')