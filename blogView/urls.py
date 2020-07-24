from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index , name='main'),
    path('blog/<int:id>/', views.post , name='post'),
]