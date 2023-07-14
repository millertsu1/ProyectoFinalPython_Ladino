from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Book, Course, Avatar, Tag, Post
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, update_session_auth_hash
from django.contrib.auth.models import User
from libreria.forms import UserEditForm, ChangePasswordForm, AvatarForm
from django.contrib import messages

# Create your views here.

def home(request):
    post = Post.objects.all()
    avatar = getavatar(request)
    return render(request, 'home.html', {'avatar': avatar,'post':post})

def us(request):
    avatar = getavatar(request)
    return render(request, 'us.html', {'avatar': avatar})

def blog(request):
    post = Post.objects.all()
    avatar = getavatar(request)
    return render(request, 'blog.html', {'avatar': avatar,'post': post})



""" access to books """
@login_required
def books(request):
    books = Book.objects.all()
    avatar = getavatar(request)
    return render(request, 'books/index.html', {'books': books, 'avatar': avatar})

@login_required
def create(request):
    form = BookForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "book created successfully")
        return redirect('books')
    avatar = getavatar(request)
    return render(request, 'books/create.html', {'form':form, 'avatar':avatar})

@login_required
def edit(request, id):
    book = Book.objects.get(id=id)
    form = BookForm(request.POST or None, request.FILES or None, instance=book)
    if form.is_valid() and request.method =='POST':
        form.save()
        messages.success(request, "Modified successfully")
        return redirect('books')
    return render(request, 'books/edit.html', {'form':form})

@login_required
def remove(request, id):
    book = Book.objects.get(id=id)
    book.delete()
    messages.success(request, "Delete successfully")
    return redirect('books')

""" access to courses"""
@login_required
def courses(request):
    courses = Course.objects.all()
    avatar = getavatar(request)
    return render(request, 'courses/index.html', {'courses': courses, 'avatar': avatar})

@login_required
def create_course(request):
    form = CourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        messages.success(request, "course created successfully")
        return redirect('courses')
    avatar = getavatar(request)
    return render(request, 'courses/create.html', {'form': form,'avatar':avatar})

@login_required
def edit_course(request, id):
    course = Course.objects.get(id=id)
    form = CourseForm(request.POST or None, request.FILES or None, instance=course)
    if form.is_valid() and request.method =='POST':
        form.save()
        messages.success(request, "Modified successfully")
        return redirect('courses')
    return render(request, 'courses/edit.html', {'form': form})

@login_required
def remove_course(request, id):
    course = Course.objects.get(id=id)
    course.delete()
    messages.success(request, "delete successfully")
    return redirect('courses')


def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method =='POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()
            messages.success(request, "user register successfully")
            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            login(request, user)
            return redirect('home')
        else:
            data['form'] = user_creation_form
    return render(request, 'registration/register.html', data)


def exit(request):
    logout(request)
    return redirect('home')


@login_required
def profile(request):
    avatar = getavatar(request)
    return render(request, 'registration/profile.html',{'avatar': avatar})

@login_required
def editProfile(request):
    user = request.user
    user_basic_info = User.objects.get(id = user.id)
    if request.method =="POST":
        form = UserEditForm(request.POST, instance = user )
        if form.is_valid():
            user_basic_info.username = form.cleaned_data.get('username')
            user_basic_info.email = form.cleaned_data.get('email')
            user_basic_info.first_name = form.cleaned_data.get('first_name')
            user_basic_info.last_name = form.cleaned_data.get('last_name')
            user_basic_info.save()
            avatar = getavatar(request)
            return render(request, 'registration/profile.html',{'avatar': avatar})
    else:
        form = UserEditForm(initial = {'username': user.username, 'email': user.email, 'first_name': user.first_name, 'last_name': user.last_name})
        avatar = getavatar(request)
        return render(request, 'registration/editProfile.html', {"form": form, 'avatar': avatar})

@login_required
def changePassword(request):
    user = request.user 
    if request.method =="POST":
        form = ChangePasswordForm(data = request.POST, user = request.user)
        if form.is_valid():
            if  request.POST['new_password1'] == request.POST['new_password2']:
                user = form.save()
                update_session_auth_hash(request, user)
            return HttpResponse('Passwords do not match')
        return render(request, 'home.html')
    else:
        form = ChangePasswordForm(user = user)
        avatar = getavatar(request)
        return render(request, 'registration/changePassword.html', {"form": form,'avatar':avatar})
    
@login_required
def changeAvatar(request):
    if request.method == 'POST':
        form = AvatarForm(request.POST, request.FILES)
        print(form)
        print(form.is_valid())
        if form.is_valid():
            user = User.objects.get(username = request.user)
            avatar = Avatar(user = user, image = form.cleaned_data['avatar'], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
                avatar = avatar[0].image.url
            except:
                avatar = None
            return render(request, 'home.html', {'avatar': avatar})
        else:
            try:
                avatar = Avatar.objects.filter(user = request.user.id)
                form = AvatarForm()
            except:
                form = AvatarForm()
        return render(request, 'avatar.html', {'form': form, 'avatar':avatar})
    form = AvatarForm()
    avatar = getavatar(request)
    return render(request, 'registration/avatar.html', {'form': form, 'avatar':avatar})


def getavatar(request):
    avatar = Avatar.objects.filter(user = request.user.id)
    try:
        avatar = avatar[0].image.url
    except:
        avatar = None
    return avatar
        
@login_required
def insertPost(request):
    #posts = Post.objects.all()
    posts = Post.objects.filter(state=True)

    form = PostForm()
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('/')
    avatar = getavatar(request)
    context = {'form': form, 'posts': posts, 'avatar':avatar}
    return render(request, 'posts/index.html', context)

#@login_required
def post(request, pk):
    post = Post.objects.get(id=pk)
    avatar = getavatar(request)
    comments = Comment.objects.filter(post=post)
    form = PostForm()
    context = {'post':post,'avatar':avatar, 'comments':comments, 'forms': form}
    return render (request, 'posts/post.html', context)

@login_required
def editPost(request, pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method =='POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
        return redirect('home')
    avatar = getavatar(request)
    context ={'form':form,'avatar':avatar}
    return render(request, 'posts/index.html', context)

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.post = post
            new_form.save()
    else:
        form = CommentForm
    return render(request, ' posts/post.html',{'post':post,'comments':comments, 'form':form })


