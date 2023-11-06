from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from base.models import base_models

# Create your views here.


def login(request):
    '''funct. for selecting user type'''
    return render(request, 'User_select_login.html')


def register(request):
    '''function for registering new user to app.'''
    if request.method == 'POST':
        # get form data
        username = request.POST['first_name']
        email=request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        user_type = request.POST['user_type']
        address = request.POST['address']


        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username is already taken')
                return redirect('register')
            else:
                # create user and profile objects
                user = User.objects.create_user(
                    username=username, password=password, email=email)
                user.save()
                profile = base_models.objects.create(
                    user=user, user_type = user_type, address = address)
                profile.save()
                messages.success(request, 'Account created successfully.')
                return render(request, 'User_select_login.html')

        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect('register')

    return render(request, 'register.html')
