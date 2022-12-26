from django.urls import path 
from . import views

# define the urls
urlpatterns = [
    path('plants/', views.plants),
    path('plant/<str:uid>', views.get_plant_by_uid),
]