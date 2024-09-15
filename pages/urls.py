from django.urls import path
from . import views
# . Represents curent path, thus importing from the current path

# URL configuration
urlpatterns = [
    path('', views.contact_view, name='contact-view'),
    path('create/', views.contact_create, name='contact-create'),
    path('create/<int:id>/', views.render_selected, name='contact-update'),
    # path('create/<int:id>/', views.contact_create, name='contact-update'),
    path('delete/<int:id>/', views.contact_delete, name='contact-delete'),
]
