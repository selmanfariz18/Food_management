from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from base.models import base_models

# Create your views here.


def user_login(request):
    '''function for normal user login'''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request=request, username=username, password=password)

        if user is not None and not user.is_superuser:
            # Check the user's user_type from the base_models model
            try:
                user_type = base_models.objects.get(user=user).user_type
                if user_type == 'normal_user':
                    login(request, user)
                    # Redirect to the desired page upon successful login
                    return HttpResponseRedirect(reverse("user_home"))
                else:
                    messages.error(request, "You are not allowed to log in.")
            except base_models.DoesNotExist:
                messages.error(request, "User type information not found.")
        else:
            messages.error(request, "Username or Password doesn't exist!!")

        return render(request, 'user_login.html')
    else:
        return render(request, 'user_login.html')

def user_logout(request):
    logout(request)
    messages.success(request, "Logout Successfull!")
    return render(request, 'user_login.html')

def user_home(request):
    return render(request, 'user_home.html')