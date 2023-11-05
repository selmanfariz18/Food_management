from django.urls import path
from users import views

urlpatterns = [
    path('login',views.user_login,name="user_login"),
]
