from django.urls import path, re_path
from . import views

urlpatterns=[
    path('test', views.test),
    re_path(r'([0-9]+)', views.number),
]