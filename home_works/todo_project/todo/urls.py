from django.urls import path

from .services import add_item, delete_item
from .views import TodoListView


urlpatterns = [
    path("", TodoListView.as_view()),
    path("add/", add_item),
    path("delete/<int:item>", delete_item),
]
# отсутствовал импорт add_item и delete_item,
# пропущено .as_view() у TodoListView
# лишний / перед todo/delete/<int:item>
