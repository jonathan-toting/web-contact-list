from django.urls import path
from . import views
# . Represents curent path, thus importing from the current path

# URL configuration
urlpatterns = [
    # path('hello/', views.say_hello),
    path('contacts/', views.index),
    path('contacts/index_style/', views.index),
    path('contacts/index_behavior/', views.index),
    path('contacts/sampleWebpage/', views.sampleWebpage)
]
