from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

# Create your views here.


def user_login(request):
    '''funct for normal user login'''
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(
            request=request, username=username, password=password)
        if user is not None:
            if user.is_superuser:
                messages.error(request, "Error in login")
                return render(request, 'user_login.html')
            else:
                login(request=request, user=user)
                #return HttpResponseRedirect(reverse("base"))
                return
        else:
            messages.error(request, "Error in login")
            return render(request, 'user_login.html')
    else:
        return render(request, 'user_login.html')