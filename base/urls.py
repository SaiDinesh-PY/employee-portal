from django.urls import path
from . import views
urlpatterns=[
    path('',views.home,name="home"),
    path('talks',views.add_talk,name="add"),
    path('notify',views.my_notifications,name="notify"),
    path('sender/<int:pk>',views.sender,name="sender"),
    path('send',views.send,name="send"),
    path('addco',views.addco,name="addco"),
    path('colleagues',views.colleagues,name='cole'),
    path('check',views.checkit,name='check'),
    path('about/',views.about,name="about")
]