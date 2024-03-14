from .models import TodoListItem
from django.views.generic import ListView


class TodoListView(ListView):
    model = TodoListItem
    template_name = "index.html"  # пропущено расширение .html
