from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect ,HttpResponse
from .forms import UserRegistrationForm, UserLoginForm
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_protect
from django.utils.decorators import method_decorator
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from django.http import HttpResponseBadRequest
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

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
        # print('post data')
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('post done sucessfully {}'.format(username))  # Replace 'home' with your desired homepage URL
            else:
                # form.add_error(None, 'Invalid username or password')
                errors = form.errors.as_json()
            return HttpResponseBadRequest('Invalid username or password')
    else:
        form = UserLoginForm()
    return HttpResponse('post not done sucessfully')

@ensure_csrf_cookie
def logout_view(request):
    logout(request)
    return redirect('login')


@method_decorator(csrf_protect, name='dispatch')
class CustomTokenRefreshView(TokenObtainPairView):
    # def post(self, request, *args, **kwargs):
    #     # Get the CSRF token from the request headers
    #     csrf_token = request.META.get('HTTP_X_CSRFTOKEN')
    #     # Set the CSRF token for the current request
        # get_token(request)
    #     # Proceed with token refresh
    #     return super().post(request, *args, **kwargs)
    pass



