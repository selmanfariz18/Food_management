from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from base.models import base_models, Food, Quote

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

import random
def user_home(request):
    '''user homepage arranging function'''
    user = request.user
    quotes = Quote.objects.all()
    if quotes:
        random_quote = random.choice(quotes)
    else:
        random_quote = None

    context = {
        'user': user,
        'quote': random_quote,
        }
    return render(request, 'user_home.html', context)


def user_contribute(request):
    '''function for contributing food'''
    if request.method == 'POST':
        # get form data
        food_name = request.POST['food_name']
        quantity=request.POST['quantity']
        date = request.POST.get('date', None)
        user = request.user


        food = Food(given_by=user, food_name=food_name, quantity=quantity, date=date)
        food.save()
        messages.info(request,'Food Contributed successfully')
        return HttpResponseRedirect(reverse("user_home"))

    return render(request, 'user_contribute.html')