from django.contrib.auth import login, logout
from django.shortcuts import render, redirect

from core.forms import SignInForm, SignUpForm


def home(request):
    return render(request, 'core/home.html')


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('edu:home')
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})


def signin_view(request):
    if request.user.is_authenticated:
        return redirect('edu:home')
    if request.method == 'POST':
        form = SignInForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            next_url = request.GET.get('next', 'edu:home')
            return redirect(next_url)
    else:
        form = SignInForm()
    return render(request, 'core/signin.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('core:login')
