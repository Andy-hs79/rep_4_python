from .models import TodoListItem
from django.http import HttpResponseRedirect


def add_item(request):
    text = request.POST.get("content")
    new_item = TodoListItem(content=text)
    new_item.save()  # было пропущено
    return HttpResponseRedirect(redirect_to="/todo")  # todo/


def delete_item(request, item):
    obj = TodoListItem.objects.get(pk=item)
    obj.delete()  # missing ()
    return HttpResponseRedirect(redirect_to="/todo")  # todo/
