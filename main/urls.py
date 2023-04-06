from django.urls import path
from . import views


urlpatterns = [
    path('', views.userLogin, name='login'),
    path('login_ar', views.userLogin_ar, name='login_ar'),
    path('logout/', views.userLogout, name='logout'),
    path('no_permission/', views.No_Permission, name='no_permission'),
    path('home/', views.home, name='home'),
    path('user_profile/', views.user_profile, name='user_profile'),
]