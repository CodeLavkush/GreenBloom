from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Username", "required" : True}))
    password = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={"placeholder" : "Password", "required" : True}))


    def clean_username(self):
        username = self.cleaned_data.get('username')

        if any(char.isdigit() for char in username):
            raise forms.ValidationError("Username does not match.")
        return username
    
class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"placeholder" : "Username", "required" : True}))
    email = forms.EmailField(max_length=100, widget=forms.EmailInput(attrs={"placeholder" : "Email", "required" : True}))
    password1 = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={"placeholder" : "Password", "required" : True}))
    password2 = forms.CharField(max_length=10, widget=forms.PasswordInput(attrs={"placeholder" : "Confirm password", "required" : True}))

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if any(char.isdigit() for char in username):
            raise forms.ValidationError("Username cannot contain numbers.")

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Username is already taken.")
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Email is already registered.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data




