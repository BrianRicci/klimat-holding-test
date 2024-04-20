from django.shortcuts import render, HttpResponse


def coffee_house_list(request):
    """Список кофеен"""
    ...


def coffee_house_details(request, coffee_house_slug):
    """Подробнее о кофейне"""
    ...


def coffee_house_add(request):
    """Добавить кофейню"""
    ...


def coffee_house_edit(request, coffee_house_slug):
    """Редактировать кофейню"""
    ...
