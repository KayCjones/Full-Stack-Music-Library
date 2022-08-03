from django.urls import path
from . import views
from urllib import request

urlpatterns = [
    path('music/', views.songs_list),
    path('<int:pk>/', views.songs_detail),
]