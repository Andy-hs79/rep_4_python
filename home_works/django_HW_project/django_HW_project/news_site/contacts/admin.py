from django.contrib import admin
from .models import Name, Phone, Book, Author

admin.site.register(Name)
admin.site.register(Phone)
admin.site.register(Book)
admin.site.register(Author)

# Register your models here.
