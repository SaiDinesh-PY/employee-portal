from django.urls import path
from authen import views

urlpatterns=[
    path('',views.login_,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logout_,name='logout'),
    path('profile/',views.profile,name='profile'),
]