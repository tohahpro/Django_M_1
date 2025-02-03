from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User, Permission, Group
from django import forms
import re
from tasks.forms import StyleForMixin
from django.contrib.auth.forms import AuthenticationForm

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']
    def __init__(self, *args, **kwargs):   # init method amader ke customize korte sahajjo korbe.
        super(UserCreationForm, self).__init__(*args, **kwargs)  # jehetu amra Usercreation form er sathe nije theke costomize korbo tar jonno self keu nita hobe.

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None

class CustomRegistrationForm(StyleForMixin,forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password', 'confirm_password']
    
    # Field error 
    def clean_password(self):
        password = self.cleaned_data.get('password')        
        errors=[]

        if len(password) < 8:
            errors.append('Password must be at least 8 character long')
        if not re.search(r'[A-Z]',password):
            errors.append('Password must include at least one uppercase letter.')
        if not re.search(r'[a-z]',password):
            errors.append('Password must include at least one lowercase letter.')
        if not re.search(r'[@#$%^&+=]',password):
            errors.append('Password must include at least one special character.')
        if not re.search(r'[0-9]',password):
            errors.append('Password must include at least one number.')        
        if errors:
            raise forms.ValidationError(errors)
        
        return password 

    def clean_email(self):
        email = self.cleaned_data.get('email')  
        email_exists = User.objects.filter(email=email).exists()

        if email_exists:
            raise forms.ValidationError("Email already exists")
        
        return email

    #  Non-Field Errors
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("Password do not match")
        
        return cleaned_data

class LoginForm(StyleForMixin, AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.apply_styled_widgets()
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

class AssignRoleForm(forms.Form):
    role = forms.ModelChoiceField(
        queryset=Group.objects.all(),
        empty_label="Select a Role"
    )