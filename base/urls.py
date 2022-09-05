from django.urls import path
from  . import views

urlpatterns = [
    path('newproject/', views.newproject, name="newproject"),
    path('interview/', views.interview, name="interview"),
]