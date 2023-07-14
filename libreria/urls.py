from django.urls import path
from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
from .views import exit, register, profile, editProfile, changePassword, changeAvatar

urlpatterns = [
    path('', views.home, name='home'),
    path('us', views.us, name='us'),
    path('blog', views.blog, name='blog'),
    path('books', views.books, name='books'),
    path('courses', views.courses, name='courses'),
    path('books/create', views.create, name='create'),
    path('books/edit', views.edit, name='edit'),
    path('books/edit/<int:id>', views.edit, name='edit'),
    path('books/delete/<int:id>', views.remove, name='remove'),
    path('courses/create', views.create_course, name='create_course'),
    path('courses/edit/<int:id>', views.edit_course, name='edit_course'),
    path('courses/edit', views.edit_course, name='edit_course'),
    path('courses/delete/<int:id>', views.remove_course, name='remove_course'),
    path('logout/', exit, name='exit'),
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('editProfile/', editProfile, name='editProfile'),
    path('changePassword/', changePassword, name='changePassword'),
    path('changeAvatar/', changeAvatar, name='changeAvatar'),

    path('posts/', views.insertPost, name='insertUrl'),
    path('posts/<int:pk>/', views.post, name='post'),
    path('posts/<int:pk>/edit/', views.editPost, name='editUrl'),




]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)