from django.urls import path
from . import views

app_name = 'menu'

urlpatterns = [
    # Эндпоинты меню - Menu
    path('add/', views.menu_add, name='menu_add'),  # добавление меню
    path('<slug:menu_slug>/', views.menu_details,
         name='menu_details'),  # подробнее о меню
    path('<slug:menu_slug>/edit/', views.menu_edit,
         name='menu_edit'),  # редактирование меню
    path('<slug:menu_slug>/delete/', views.menu_delete,
         name='menu_delete'),  # удаление меню

    # Эндпоинты позиций - MenuItems
    path('<slug:menu_slug>/items/add/', views.menu_item_add,
         name='menu_item_add'),  # добавление позиции
    path('<slug:menu_slug>/items/<int:item_id>/', views.menu_item_details,
         name='menu_item_details'),  # подробнее о позиции
    path('<slug:menu_slug>/items/<int:item_id>/edit/', views.menu_item_edit,
         name='menu_item_edit'),  # редактирование позиции
    path('<slug:menu_slug>/items/<int:item_id>/delete/', views.menu_item_delete,
         name='menu_item_delete'),  # удаление позиции
]
