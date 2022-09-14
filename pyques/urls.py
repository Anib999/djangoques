from django.urls import path
from . import views

urlpatterns = [
    path('', views.simpleques, name="simpleques"),
    path('simplequesans/', views.simplequesans, name="simplequesans"),
    path('oop/', views.oop, name="oop"),
    path('oopans/', views.oopans, name="oopans"),
]