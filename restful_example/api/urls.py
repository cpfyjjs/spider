from django.urls import path
from django.urls import re_path
from api import views

urlpatterns = [
    path('index/',views.MovieView.as_view()),
    path('login/',views.LogView.as_view()),

]