from django.urls import path
from users import views

urlpatterns = [
    path('user_login',views.user_login,name="user_login"),
    path('user_logout',views.user_logout,name="user_logout"),
    path('user_home', views.user_home, name="user_home"),
    path('user_contribute', views.user_contribute, name="user_contribute"),

]
