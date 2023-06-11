from django.urls import path
from . import views


urlpatterns = [
    path('all-cafes/', views.all_cafes, name = 'all_cafes'),
    path('random-cafe/', views.random_cafe, name = 'random_cafe'),
    path('all-cafes/', views.cafe_by_location, name = 'cafe_by_location'),
    path('delete-cafe/', views.delete_cafe, name = 'delete_cafe'),
    path('update-price/', views.update_price, name = 'update_price'),
    path('add-cafe/', views.add_cafe, name = 'add_cafe'),
]
