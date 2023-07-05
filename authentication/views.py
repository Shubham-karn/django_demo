from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect ,HttpResponse
from .models import UserRegistrationForm, UserLoginForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.http import HttpResponseBadRequest

@ensure_csrf_cookie
def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse('post done sucessfully')
        
        else:
            errors = form.errors.as_json()
            return HttpResponseBadRequest(errors)
    else:
        form = UserRegistrationForm()
    return HttpResponse('post not done sucessfully')

@ensure_csrf_cookie
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # Replace 'home' with your desired homepage URL
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})

@ensure_csrf_cookie
def logout_view(request):
    logout(request)
    return redirect('login')