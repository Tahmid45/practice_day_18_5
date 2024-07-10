
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_pass/', views.pass_change, name='passChange'),
    path('change_pass2/', views.pass_change2, name='passChange2'),
]
