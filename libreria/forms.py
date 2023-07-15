from django import forms
from django.forms import ModelForm
from .models import Book, Course, Post, Comment
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('This email is already registered')
        return email
    

class UserEditForm(UserChangeForm):
    username = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Username"}))
    email = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Email"}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"First_name"}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"Last_name"}))

    class Meta:
        model = User
        fields = ['username','email','first_name','last_name']
        help_texts ={k:"" for k in fields}

class ChangePasswordForm(PasswordChangeForm):
    old_password = forms.CharField(label = "", widget=forms.PasswordInput(attrs={"placeholder":"Old Password"}))
    new_password1 = forms.CharField(label = "", widget=forms.PasswordInput(attrs={"placeholder":"New Password"}))
    new_password2 = forms.CharField(label = "", widget=forms.PasswordInput(attrs={"placeholder":"Confirm New Password"}))
    

    class Meta:
        model = User
        fields = ['old_password','new_password1','new_password2']
        help_texts ={k:"" for k in fields}

class AvatarForm(forms.Form):
    avatar = forms.ImageField()

class PostForm(ModelForm):

    class Meta:
        model = Post
        fields ='__all__'

        widgets = {'tags': forms.CheckboxSelectMultiple(),}

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('author','content','active')
        