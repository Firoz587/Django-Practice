from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
    path('profile/',views.profile,name='profile'),
    path('pass_change/', views.pass_change, name='passchange'),
     path('logout/', views.user_logout, name='logout'),
]
