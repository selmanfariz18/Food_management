from django.urls import path
from base import views

urlpatterns = [
    path('', views.login,name="login"),
    path('register',views.register, name="register"),
]
