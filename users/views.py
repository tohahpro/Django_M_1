from django.shortcuts import render, redirect, HttpResponse  
from django.contrib.auth.models import User, Group
from users.forms import CustomRegistrationForm 
from django.contrib.auth import login, logout
from django.contrib import messages
from users.forms import LoginForm, AssignRoleForm, CreateGroupForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.decorators import login_required, user_passes_test
# Create your views here.

# Test for Users
def is_admin(user):
    return user.groups.filter(name='Admin').exists()

def sign_up(request):
    if request.method == 'GET':
        # form = RegisterFrom()
        form = CustomRegistrationForm()
    if request.method == 'POST':
        # form = RegisterFrom(request.POST)
        form = CustomRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data.get('password'))
            user.is_active = False
            user.save()
            messages.success(request, 'A confirmation mail send. Please check your email')
            return redirect('sign-in')
        else:
            print('Form is not valid')

    return render(request, 'registration/register.html',{'form':form})

def sign_in(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():        
            user = form.get_user()
            login(request, user)
            return redirect('home')        
    return render(request, 'registration/login.html',{'form':form})

@login_required
def sign_out(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')
# USER ACTIVE
def active_user(request, user_id, token):
    try:
        user = User.objects.get(id=user_id)
        if default_token_generator.check_token(user, token):
            user.is_active= True
            user.save()
            return redirect('sign-in')
        else:
            return HttpResponse('Invalid user or id')
    except User.DoesNotExist:
        return HttpResponse('User not found')

@user_passes_test(is_admin)
def admin_dashboard(request):
    users = User.objects.all()
    return render(request, 'admin/dashboard.html',{'users':users})

@user_passes_test(is_admin)
def assign_role(request, user_id):
    user = User.objects.get(id=user_id)
    form = AssignRoleForm()

    if request.method == 'POST':
        form = AssignRoleForm(request.POST)
        if form.is_valid():
            role = form.cleaned_data.get('role')
            user.groups.clear() # Remove old role
            messages.success(request, f"User {user.username} has been assigned to the {role.name} role.")
            return redirect('admin-dashboard')
    return render(request, 'admin/assign_role.html',{'form':form})

@user_passes_test(is_admin)
def create_group(request):
    form = CreateGroupForm()
    if request.method == 'POST':
        form = CreateGroupForm(request.POST)
        if form.is_valid():
            group = form.save()
            messages.success(request, f'Group {group.name} has been created successfully.')
            return redirect('create-group')
    return render(request, 'admin/create_group.html',{'form':form})

@user_passes_test(is_admin)
def group_list(request):
    groups = Group.objects.all()
    return render(request, 'admin/group_list.html',{'groups': groups})