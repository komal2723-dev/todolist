from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm,PasswordResetForm
from django.contrib.auth.models import User
from .models import Task
class registraitonform(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':"form-control border border-dark border-2", 'id':"exampleInputPassword1",'type':"password"}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your Username','class':"form-control border border-dark border-2", 'id':"exampleInputUsername1", 'type':"text"}))
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your Email', 'class':"form-control border border-dark border-2", 'id':"exampleInputEmail1", 'type':"email",'aria-describedby':"emailHelp"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':"form-control border border-dark border-2", 'id':"exampleInputpassword2",'type':"password"}))
    class Meta:
        model = User
        fields = ['username', 'email','password1']
        


class AuthenticationForm(AuthenticationForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':"form-control border border-dark border-2", 'id':"exampleInputPassword",'type':"password"}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your Username','class':"form-control border border-dark border-2", 'id':"exampleInputUsername1", 'type':"text"}))
    class Meta:
        model=User
        fields=['username','password']


class TodoForm(forms.ModelForm):
    title=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'What is the task today?','class':"form-control border border-dark border-2", 'id':"exampletitle", 'type':'text'}))
    class Meta:
        model=Task
        fields=['title']

class ForgotPasswordForm(PasswordResetForm):
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your Email address', 'class':"form-control border border-dark border-2", 'id':"exampleInputEmail1", 'type':"email",'aria-describedby':"emailHelp"}))
    class Meta:
        model = Task
        fields = ['email']


class verifycodeform(forms.Form):
    code=forms.CharField(max_length=6,label='Verification Code',widget=forms.TextInput(attrs={'placeholder':'Enter Verification Code','class':"form-control border border-dark border-2", 'id':"exampleCode","type":"number"}))

class setPasswordForm(forms.Form):
    new_password1 = forms.CharField(label='New Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter New Password','class':"form-control border border-dark border-2", 'id':"exampleInputPassword1",'type':"password"}))
    new_password2 = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput(attrs={'placeholder':'Re-enter New Password','class':"form-control border border-dark border-2", 'id':"exampleInputpassword2",'type':"password"}))