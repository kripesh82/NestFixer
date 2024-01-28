from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.forms import PasswordChangeForm

class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize the widget attributes for password fields
        self.fields['old_password'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'
        self.fields['new_password1'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'
        self.fields['new_password2'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'


class EditProfileForm(UserChangeForm):
    class Meta:
        model = User
        fields = ('username', 'email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Customize form fields if needed
        self.fields['username'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter your username'

        self.fields['email'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'
        self.fields['email'].widget.attrs['placeholder'] = 'Enter your email'

        
        # Check for the correct field names for password change
        if 'password' in self.fields:
            self.fields['password'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'
        if 'new_password1' in self.fields:
            self.fields['new_password1'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'
        if 'new_password2' in self.fields:
            self.fields['new_password2'].widget.attrs['class'] = 'w-full py-4 px-6 rounded-xl'





class LoginForm(AuthenticationForm):
    
    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
    
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))
     


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields=('username' , 'email' , 'password1' , 'password2')

    username=forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Enter Username',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    email=forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder': 'Enter Email',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password1=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Enter Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    password2=forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Confirm Password',
        'class': 'w-full py-4 px-6 rounded-xl'
    }))

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        password2 = cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords do not match.")

        return cleaned_data
