from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='index'),
    path('account/<str:ano>/',views.account,name='account'),
    path('transfermoney/',views.transfermoney,name='transfermoney'),
    path('about/',views.about,name='about'),
]