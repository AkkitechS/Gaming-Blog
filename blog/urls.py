# pip install -r requirements.txt

from django.urls import path
from . import views

urlpatterns = [
    path('article/<int:id>', views.blogView)
]