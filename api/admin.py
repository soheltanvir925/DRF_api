from django.contrib import admin
from .models import Student, Profile, Author, Book

# Register your models here.
admin.site.register(Student)
admin.site.register(Profile)
admin.site.register(Author)
admin.site.register(Book)