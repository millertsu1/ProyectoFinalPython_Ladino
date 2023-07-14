from django.contrib import admin
from .models import Book, Course, Avatar, Tag, Post, Comment

# Register your models here.
admin.site.register(Book)
admin.site.register(Course)
admin.site.register(Avatar)
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
