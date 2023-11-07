from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from base.models import base_models, Food, Quote
import random

# Create your views here.


def community_login(request):
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
                if user_type == 'community':
                    login(request, user)
                    # Redirect to the desired page upon successful login
                    return HttpResponseRedirect(reverse("community_home"))
                else:
                    messages.error(request, "You are not allowed to log in.")
            except base_models.DoesNotExist:
                messages.error(request, "User type information not found.")
        else:
            messages.error(request, "Username or Password doesn't exist!!")

        return render(request, 'community_login.html')
    else:
        return render(request, 'community_login.html')

def community_logout(request):
    logout(request)
    messages.success(request, "Logout Successfull!")
    return render(request, 'community_login.html')

def community_home(request):
    '''function for setting community homepage'''
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
    return render(request, 'community_home.html', context)

def community_food_watch(request):
    '''Contributed foods are displayed to community page by this view'''
    foods = Food.objects.all()
    details = base_models.objects.all()

    context = {
        'foods': foods,
        'details': details,
    }

    '''for i in foods:
        print(i.date)'''

    return render(request, 'community_food_watch.html', context)

def approve_food(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        work_instance = get_object_or_404(Food, id=id)
        work_instance.status="approved"
        work_instance.save()
        return HttpResponseRedirect(reverse("community_food_watch"))


def delete_food(request):
    if request.method == 'POST':
        id = request.POST.get("id")
        work_instance = get_object_or_404(Food, id=id)
        work_instance.status="rejected"
        work_instance.save()
        return HttpResponseRedirect(reverse("community_food_watch"))


def community_food_history(request):
    '''Approved or rejected foods history are displayed to community page by this view'''
    foods = Food.objects.all()
    details = base_models.objects.all()

    context = {
        'foods': foods,
        'details': details,
    }



    return render(request, 'community_food_history.html', context)
