from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404, redirect, render, Http404
from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser



# Custom test function to check if user has the "front_desk_manager" role
def is_front_desk_manager(user):
    return user.roles == 'front_desk_manager'

# Custom test function to check if user has the "auditor" role
def is_auditor(user):
    return user.roles == 'auditor'


@login_required
@user_passes_test(lambda u: u.is_superuser)  # Only accessible by superusers
def manage_roles(request):
    users = CustomUser.objects.exclude(is_superuser=True)  # Exclude superadmin users
    return render(request, 'manage_roles.html', {'users': users})


@login_required
@user_passes_test(lambda u: u.is_superuser)  # Only accessible by superusers
def update_role(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        new_role = request.POST['new_role']
        user.roles = new_role
        user.save()
        messages.success(request, 'User role updated successfully.')
        return redirect('manage_roles')
    else:
        return redirect('manage_roles')

# @login_required
# @user_passes_test(lambda u: is_front_desk_manager(u) or is_auditor(u))
# def restricted_view(request):
#     # View logic for restricted view accessible by front desk managers or auditors

# @login_required
# @user_passes_test(is_front_desk_manager)
# def front_desk_manager_view(request):
#     # View logic for front desk manager

# @login_required
# @user_passes_test(is_auditor)
# def auditor_view(request):
#     # View logic for auditor


def error_404_view(request, exception):
    return render(request, '404.html', status=404)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('user_list')  # Redirect to the desired page after successful login
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login')



@login_required
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('dashboard')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('dashboard')
    else:
        form = CustomUserChangeForm(instance=request.user)
    return render(request, 'profile.html', {'form': form})


@login_required
@user_passes_test(lambda u: is_front_desk_manager(u) or is_auditor(u))
def dashboard(request):
    return render(request, 'dashboard.html')



@login_required
def user_list(request):
    users = CustomUser.objects.exclude(is_superuser=True)
    return render(request, 'user_list.html', {'users': users})


# def create_user(request):
#     if request.method == 'POST':
#         form = CustomUserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             return redirect('user_detail', user_id=user.id)
#     else:
#         form = CustomUserCreationForm()
#     return render(request, 'create_user.html', {'form': form})

@login_required
def user_detail(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    return render(request, 'user_detail.html', {'user': user})

@login_required
def update_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            return redirect('user_detail', user_id=user.id)
    else:
        form = CustomUserChangeForm(instance=user)
    return render(request, 'update_user.html', {'form': form, 'user': user})

@login_required
@user_passes_test(lambda u: u.is_superuser)
def delete_user(request, user_id):
    user = get_object_or_404(CustomUser, id=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('dashboard')
    return render(request, 'delete_user.html', {'user': user})




