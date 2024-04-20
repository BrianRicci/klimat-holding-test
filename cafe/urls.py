from django.urls import path
from . import views

app_name = 'cafe'

urlpatterns = [
    # список всех кофеен
    path('', views.coffee_house_list, name='coffee_house_list'),

    # Эндпоинты кофеен - CoffeeHouse
    path('add_coffee_house/', views.coffee_house_add,
         name='coffee_house_add'),  # добавление кофейни
    path('<slug:coffee_house_slug>/',
         views.coffee_house_details, name='coffee_house_details'),  # подробнее о кофейне(меню, позиции)
    path('<slug:coffee_house_slug>/edit/',
         views.coffee_house_edit, name='coffee_house_edit'),  # страница редактирования кофейни
]
