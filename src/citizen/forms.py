from django.contrib.auth import authenticate
from django import forms

from .models import Citizen


class UsersLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget = forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersLoginForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name":"username"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name":"password"})

    def clean(self, *args, **keyargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username = username, password = password)
            if not user:
                raise forms.ValidationError("Invalid Credentials")

        return super(UsersLoginForm, self).clean(*args, **keyargs)




class UsersRegisterForm(forms.ModelForm):
    class Meta:
        model = Citizen
        fields = [
            "username",
            'first_name',
            'last_name',
            'birth_date',
            'aadhaar',
            'bhamashah',
            'contact',
            "email",
            "confirm_email",
            "password",
            'confirm_password'
        ]

    username = forms.CharField()
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField(label="Email")
    confirm_email = forms.EmailField(label="Confirm Email")
    confirm_password =forms.CharField(widget=forms.PasswordInput)
    password = forms.CharField(widget=forms.PasswordInput)

    def __init__(self, *args, **kwargs):
        super(UsersRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            "name": "username"})
        self.fields['email'].widget.attrs.update({
            'class': 'form-control',
            "name": "email"})
        self.fields['confirm_email'].widget.attrs.update({
            'class': 'form-control',
            "name": "confirm_email"})
        self.fields['password'].widget.attrs.update({
            'class': 'form-control',
            "name": "password"})

    def clean(self, *args, **keyargs):
        email = self.cleaned_data.get("email")
        confirm_email = self.cleaned_data.get("confirm_email")
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")
        confirm_password = self.cleaned_data.get("confirm_password")
        aadhaar = self.cleaned_data.get("aadhaar")
        bhamashah = self.cleaned_data.get("bhamashah")

        if email != confirm_email:
            raise forms.ValidationError("Email must match")

        if password != confirm_password:
            raise forms.ValidationError("Password must match")

        email_qs = Citizen.objects.filter(email=email)
        if email_qs.exists():
            raise forms.ValidationError("Email is already registered")

        if not aadhaar.isdigit() or not len(aadhaar)==12:
            raise forms.ValidationError("Invalid Aadhar ID")

        username_qs = Citizen.objects.filter(username=username)
        if username_qs.exists():
            raise forms.ValidationError("User with this username already registered")

        if len(password) < 8:  # you can add more validations for password
            raise forms.ValidationError("Password must be greater than 8 characters")

        return super(UsersRegisterForm, self).clean(*args, **keyargs)
