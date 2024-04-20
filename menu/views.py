from django.shortcuts import render, redirect
from .models import Menu, MenuItem
from .forms import MenuForm, MenuItemForm
from cafe.models import CoffeeHouse


# Блок меню
def menu_details(request, menu_slug):
    """Подробнее о меню"""
    ...


def menu_add(request, coffee_house_slug):
    """Добавить меню"""
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.coffee_house_id = CoffeeHouse.objects.get(
                slug=coffee_house_slug).id
            menu.save()
            return redirect('cafe:coffee_house_details', coffee_house_slug=coffee_house_slug)
    else:
        form = MenuForm()
    return render(request, 'menu/add.html',
                  {'form': form,
                   'coffee_house_slug': coffee_house_slug})


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
