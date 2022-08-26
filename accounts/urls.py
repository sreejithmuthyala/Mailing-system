from django.urls import path
from . import views

urlpatterns = [
    path('', views.lore, name='lore'),
    path('login', views.login, name='login'),
    path('register',views.register, name='register'),
    path('logout',views.logout, name='logout'),
    path('compose',views.compose, name='compose'),
    path('inbox',views.inbox, name='inbox'),
    path('sent',views.sent,name='sent'),
]
