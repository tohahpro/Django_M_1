from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User
from django import forms
import re

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']
    def __init__(self, *args, **kwargs):   # init method amader ke customize korte sahajjo korbe.
        super(UserCreationForm, self).__init__(*args, **kwargs)  # jehetu amra Usercreation form er sathe nije theke costomize korbo tar jonno self keu nita hobe.

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password', 'confirm_password']
    
    # Field error 
    def clean_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        errors=[]

        if len(password) < 8:
            errors.append('Password must be at least 8 character long')
        if re.fullmatch(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*()_+])[A-Za-z\d@#$%^&*()_+]', password):
            errors.append('Password must include Uppercase, Lowercase, number & special character')
        if password != confirm_password:
            errors.append('Password do not match')
        if errors:
            raise forms.ValidationError(errors)
        
        return password   

    #  Non-Field Errors
    # def clean(self):
    #     cleaned_data = super().clean()
    #     password = cleaned_data.get('password')
    #     confirm_password = cleaned_data.get('confirm_password')

    #     if password != confirm_password:
    #         raise forms.ValidationError("Password do not match")
        
    #     return cleaned_data