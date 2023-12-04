from django.contrib import admin
from django.urls import path,include
from myapp import views
urlpatterns = [
    path('signup',views.signup,name="signup"),
    path('',views.home,name="home"),
    path('login',views.loginuser,name="login"),
    path('logout', views.logoutUser, name="logout"),

]
