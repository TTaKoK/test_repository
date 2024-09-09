from django.shortcuts import render
from django.http import HttpResponse

#ビュー関数
def index(request):
    return HttpResponse("Hello World. You're at the polls index.")
