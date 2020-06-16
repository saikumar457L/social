from django import forms

from django.contrib.auth.models import User
from .models import Profile


class UserRegistrationForm(forms.ModelForm):

    password = forms.CharField(label="Password",widget=forms.PasswordInput)
    password2 = forms.CharField(label="Confirm Password",widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username',"email","first_name"]
        widgets = {
            'username':forms.TextInput(attrs={
                'required':True,
                'placeholder':"Username"
            }),
            'first_name':forms.TextInput(attrs={
                'required':False,
                'placeholder':"First Name"
            }),
            "email":forms.TextInput(attrs={
                'required':True,
                'placeholder':"Email"
            })
        }

        def clean_password(self):
            cd = self.cleaned_data

            if cd['password'] != cd['password2']:

                raise forms.ValidationEror("Passwords didn't match please try again.")

            return cd['password2']

        def clean_email(self):
            email = self.cleaned_data.get('email')
            username = self.cleaned_data.get("username")

            email_check = User.objects.filter(email__iexact=email).exists()

            if email_check:
                raise forms.ValidationEror("The given Mail is already taken. Please try another one.")


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name","last_name","email"]

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["date_of_birth","photo","gender"]
