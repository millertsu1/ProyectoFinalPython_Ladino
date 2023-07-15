from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/',verbose_name='Book Image', null=True)
    description = models.TextField(null=True, verbose_name='Description')

    def __str__(self):
        row = "Title: " + self.title + " - " + "Description: " + self.description
        return row
    
    def delete(self, using=None, keep_parents=False):
        self.image.storage.delete(self.image.name)
        super().delete()


class Course(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, verbose_name='Title')
    image = models.ImageField(upload_to='images/',verbose_name='Course Image', null=True)
    description = models.TextField(null=True, verbose_name='Description')
    
    def __str__(self):
        row2 = "Title: " + self.title + " - " + "Description: " + self.description
        return row2

class Avatar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profile')
    image = models.ImageField(upload_to='avatares', null = True, blank=True, default='avatar.png')


class Tag(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextField(null=True, blank=True)
    #body = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True, upload_to='images', default='placeholder.png')
    state = models.BooleanField('Active', default=False)
    tags = models.ManyToManyField(Tag, blank=True)
    author = models.CharField(max_length=100, null=True, blank=True,)

    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['-id']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,related_name='comments')
    author = models.CharField(max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    #content = RichTextField(null=True, blank=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f"comment by {self.author}{self.content}"









