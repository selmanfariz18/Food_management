from django.urls import path
from communities import views

urlpatterns = [
    path('community_login',views.community_login,name="community_login"),
    path('community_logout',views.community_logout,name="community_logout"),
    path('community_home', views.community_home, name="community_home"),
    path('community_food_watch', views.community_food_watch, name="community_food_watch"),
    path('delete_food', views.delete_food, name="delete_food"),
    path('approve_food', views.approve_food, name="approve_food"),
    path('community_food_history', views.community_food_history, name="community_food_history"),
]
