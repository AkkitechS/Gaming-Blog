from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('about/', views.about),
    path('contact/', views.contact),
    path('blogs/', views.blog),
    path('search/', views.search),
    path('register/', views.signup),
    path('login/', views.userLogin),
    path('logout/', views.userLogout),
]