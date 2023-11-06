from django.urls import path
from hotels import views

urlpatterns = [
    path('hotel_login',views.hotel_login,name="hotel_login"),
    path('hotel_logout',views.hotel_logout,name="hotel_logout"),
    path('hotel_home', views.hotel_home, name="hotel_home"),
    path('hotel_contribute', views.hotel_contribute, name="hotel_contribute"),
]
