from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.hello_world, name='hello_world'),
    url(r'^template/$', views.hello_template, name='hello_template'),
]
# r''のようにrつけるとエスケープシーンスを無視できる(raw文字列。)
#  hello Worldのビュー関数を呼び出すための設定
