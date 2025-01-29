from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.models import User

class RegisterFrom(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password1', 'password2']
    def __init__(self, *args, **kwargs):   # init method amader ke customize korte sahajjo korbe.
        super(UserCreationForm, self).__init__(*args, **kwargs)  # jehetu amra Usercreation form er sathe nije theke costomize korbo tar jonno self keu nita hobe.

        for fieldname in ['username','password1', 'password2']:
            self.fields[fieldname].help_text = None