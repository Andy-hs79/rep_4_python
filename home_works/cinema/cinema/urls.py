
from django.contrib import admin
from django.urls import path
from movie.views import MovieListView, MovieCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', MovieListView.as_view()),
    path('movie_create/', MovieCreateView.as_view()),

]
