from django.urls import path
from communities import views

urlpatterns = [
    path('community_login',views.community_login,name="community_login"),
    path('community_logout',views.community_logout,name="community_logout"),
    path('community_home', views.community_home, name="community_home"),
]
