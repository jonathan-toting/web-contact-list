from django.urls import path
from . import views
# . Represents curent path, thus importing from the current path

# URL configuration
urlpatterns = [
    path('hello/', views.say_hello),
    path('contactlist/', views.index)
]
