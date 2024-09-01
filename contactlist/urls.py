from django.urls import path
from . import views
# . Represents curent path, thus importing from the current path

# URL configuration
urlpatterns = [
    path('', views.homepage_view),
    path('create', views.contact_create_view),
]
