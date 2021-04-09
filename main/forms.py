from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django.forms import CharField, EmailField
from django.forms import widgets

class RegisterForm(UserCreationForm):
    username = CharField(max_length=60, label="Username", widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = EmailField(label="Email ID", widget=widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email Address"}))
    first_name = CharField(max_length=60, label="First Name", widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = CharField(max_length=60, label="Last Name", widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "Last Name"}))
    password1 = CharField(max_length=455, label="Password", widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password2 = CharField(max_length=455, label="Confirm Password", widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Confirm Password"}))
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

class LoginForm(AuthenticationForm):
    username = CharField(max_length=60, label="Username", widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = CharField(max_length=455, label="Password", widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    class Meta:
        model = User
        fields = ('username', 'password1')

class ChangePassword(PasswordChangeForm):
    old_password = CharField(max_length=455, label="Old Password", widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Old Password'}))
    new_password1 = CharField(max_length=455, label="New Password", widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'New Password'}))
    new_password2 = CharField(max_length=455, label="Confirm New Password", widget=widgets.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))


class ModifyDataForm(UserChangeForm):
    email = EmailField(label="Email ID", widget=widgets.EmailInput(attrs={'class': 'form-control', 'placeholder': "Email Address"}))
    first_name = CharField(max_length=60, label="First Name", widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}))
    last_name = CharField(max_length=60, label="Last Name", widget=widgets.TextInput(attrs={'class': 'form-control', 'placeholder': "Last Name"}))
    password = None
    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')