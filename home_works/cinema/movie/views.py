from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from .models import Film


class MovieListView(ListView):
    model = Film
    films = model.objects.all()
    context = {'all_films': films}
    template_name = 'index.html'
    fields = '__all__'


class MovieCreateView(CreateView):
    model = Film
    template_name = 'movie_create.html'
    fields = '__all__'
    success_url = '/index'

# Create your views here.
