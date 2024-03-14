
from django.contrib import admin
from django.urls import path
from movie.views import MovieListView, MovieCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', MovieListView.as_view()),
    path('index/', MovieListView.as_view()),
    path('movie_create/', MovieCreateView.as_view()),

]
