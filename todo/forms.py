from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class registraitonform(UserCreationForm):
    password1=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':"form-control", 'id':"exampleInputPassword1",'type':"password"}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your Username','class':"form-control", 'id':"exampleInputUsername1", 'type':"text"}))
    email = forms.EmailField(required=True, label='Email', widget=forms.TextInput(attrs={'placeholder': 'Enter your Email', 'class':"form-control", 'id':"exampleInputEmail1", 'type':"email",'aria-describedby':"emailHelp"}))
    password2 = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':"form-control", 'id':"exampleInputpassword2",'type':"password"}))
    class Meta:
        model = User
        fields = ['username', 'email','password1']
        


class AuthenticationForm(AuthenticationForm):
    password=forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'placeholder':'Enter your Password','class':"form-control", 'id':"exampleInputPassword",'type':"password"}))
    username=forms.CharField(label='Username',widget=forms.TextInput(attrs={'placeholder':'Enter your Username','class':"form-control", 'id':"exampleInputUsername1", 'type':"text"}))
    class Meta:
        model=User
        fields=['username','password']