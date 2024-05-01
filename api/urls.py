from django.urls import path, include
from .views import *


app_name = 'api'

urlpatterns = [
    # http://127.0.0.1:8000/api/v1/coffee-houses/
    path('coffee-houses/', CoffeeHouseAPIList.as_view()),
    path('coffee-houses/<int:pk>/', CoffeeHouseAPIUpdate.as_view()),
    path('coffee-houses/delete/<int:pk>/', CoffeeHouseAPIDestroy.as_view()),
    # http://127.0.0.1:8000/api/v1/menus/
    path('menus/', MenuAPIList.as_view()),
    path('menus/<int:pk>', MenuAPIUpdate.as_view()),
    path('menus/delete/<int:pk>', MenuAPIDestroy.as_view()),
    # http://127.0.0.1:8000/api/v1/menu-items/
    path('menu-items/', MenuItemAPIList.as_view()),
    path('menu-items/<int:pk>', MenuItemAPIUpdate.as_view()),
    path('menu-items/delete/<int:pk>', MenuItemAPIDestroy.as_view()),
]
