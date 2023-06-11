from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('cafes', views.show, name = 'show'),
    path('add', views.add, name = 'add'),
]
