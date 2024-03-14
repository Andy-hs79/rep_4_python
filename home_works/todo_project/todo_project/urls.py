from django.contrib import admin
from django.urls import path, include
from todo.views import TodoListView
from todo.services import add_item, delete_item


urlpatterns = [
    path("admin/", admin.site.urls),
    path("todo/", include("todo.urls")),
]
