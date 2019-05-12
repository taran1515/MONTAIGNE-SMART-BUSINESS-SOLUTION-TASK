from django import forms

from .models import Post, Comment
from django.contrib.auth.models import User
from django.forms import ValidationError

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = (
            'title',
            'body',

        )

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = (
            'text',
        )

class UserLoginForm(forms.Form):
    username = forms.CharField(label='')
    password = forms.CharField(label='',widget = forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Enter Password Here...'}))
    confirm_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm Password...'}))
    class Meta:
        model = User
        fields =(
            'username',
            'first_name',
            'last_name',
            'email',
        )
    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password!= confirm_password:
            raise forms.ValidationError("Password do not matches")
        return confirm_password
