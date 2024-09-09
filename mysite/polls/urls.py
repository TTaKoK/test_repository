from django.urls import path

from . import views

urlpatterns=[
    #第一引数routeとまっちするものを見つけた後、第二引数で指定のビュー関数を呼ぶ
    #第四引数nameはURLへの名前付け。templateでよく使う、アクセスのショトカ
    path("",views.index,name="index"),
]