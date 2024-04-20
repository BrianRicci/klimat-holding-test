from django.shortcuts import render

# Блок меню


def menu_details(request, coffee_house_slug):
    """Подробнее о меню"""
    ...


def menu_add(request, coffee_house_slug):
    """Добавить меню"""
    ...


def menu_edit(request, coffee_house_slug, menu_slug):
    """Редактировать меню"""
    ...


# Блок позиций
def menu_item_details(request, coffee_house_slug, menu_slug):
    """Подробнее о позиции"""
    ...


def menu_item_add(request, coffee_house_slug, menu_slug):
    """Добавить позицию"""
    ...


def menu_item_edit(request, coffee_house_slug, menu_slug):
    """Редактировать позицию"""
    ...
