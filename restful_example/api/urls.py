from django.urls import path
from django.urls import re_path
from api import views

urlpatterns = [
    path('movie/',views.MovieView.as_view()),
    path('movie_detail/',views.MovieDetailView.as_view()),
    path('movie_detail/<int:pk>',views.MovieDetailView.as_view()),

    path('login/',views.LogView.as_view()),

]