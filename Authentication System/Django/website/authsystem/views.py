from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from website.settings import BASE_DIR
from django.http.response import FileResponse
from .forms import RegisterForm, LoginForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.hashers import check_password
from django.contrib.auth.decorators import login_required, user_passes_test


def home(request):
    return render(request, 'index.html')


@user_passes_test(lambda user: not user.is_authenticated)
def register_user(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            if User.objects.filter(email = form.cleaned_data['email']):
                messages.error(request, 'You already have an email sign in instead')
            else:
                login(request, User.objects.create_user(form.cleaned_data['username'],
                form.cleaned_data['email'], form.cleaned_data['password']))
                return redirect('secrets')
    return render(request, 'register.html', {'form': form})


@user_passes_test(lambda user: not user.is_authenticated)
def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user = User.objects.filter(email = form.cleaned_data['email']).first()
            try:
                if check_password(form.cleaned_data['password'], user.password):
                    auth_user = authenticate(request, username = user.username, password = form.cleaned_data['password'])
                    login(request, auth_user)
                    return redirect('secrets')
                else:
                    messages.error(request, 'Your email or password is incorrect')
            except:
                messages.error(request, 'Your email or password is incorrect')
    return render(request, 'login.html', {'form': form})    


@login_required
def logout_user(request):
    logout(request)
    return redirect('home')


@login_required
def secrets(request):
    return render(request, 'secrets.html')

@login_required
def download(request):
    return FileResponse(open(BASE_DIR / 'authsystem/static/files/cheat_sheet.pdf', 'rb'), as_attachment = True)