from django.shortcuts import render

# Create your views here.


def login(request):
    '''funct. for selecting user type'''
    return render(request, 'User_select_login.html')