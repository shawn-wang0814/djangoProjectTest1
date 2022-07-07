from django.conf.urls import url
from django.contrib import admin

from bookTest import views

urlpatterns = [
    url(r'^index', views.index_view),
    # django 会把正则匹配的分组（）内容当做参数传入视图函数中
    url(r'^books/([0-9]+)$', views.detail),
    url(r"^delete/([0-9]+)$", views.delete),
    url(r"^create$", views.create),
    url(r"^create_book$", views.create_book),
    url(r'^books', views.show_books),

]