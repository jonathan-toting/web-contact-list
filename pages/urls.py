from django.urls import path
from . import views
# . Represents curent path, thus importing from the current path

# URL configuration
urlpatterns = [
    path('contacts', views.contact_view),
    path('create', views.contact_add),
    # path('update', views.contact_update),
    # path('delete', views.contact_delete),
]
