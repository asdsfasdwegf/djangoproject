from django import forms

class UserRegisterForm(forms.Form):
    Username = forms.CharField()
    Email = forms.EmailField()
    Password = forms.CharField()

class UserLoginForm(forms.Form):
    Username = forms.CharField()
    Password = forms.CharField()