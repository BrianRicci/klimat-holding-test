from django.shortcuts import render, redirect
from .models import Menu, MenuItem
from .forms import MenuForm, MenuItemForm
from cafe.models import CoffeeHouse
from services import queries


# Блок меню
def menu_details(request, coffee_house_slug, menu_slug):
    """Подробнее о меню"""
    menu = queries.get_object_by_slug(Menu, menu_slug)
    item_list = menu.items.all()
    return render(request, 'menu/details.html',
                  {'menu': menu,
                   'item_list': item_list,
                   'coffee_house_slug': coffee_house_slug,
                   'menu_slug': menu_slug})


def menu_add(request, coffee_house_slug):
    """Добавить меню"""
    if request.method == 'POST':
        form = MenuForm(request.POST)
        if form.is_valid():
            menu = form.save(commit=False)
            menu.coffee_house_id = queries.get_object_by_slug(
                CoffeeHouse, coffee_house_slug).id
            menu.save()
            return redirect('cafe:coffee_house_details', coffee_house_slug=coffee_house_slug)
    else:
        form = MenuForm()
    return render(request, 'menu/add.html',
                  {'form': form,
                   'coffee_house_slug': coffee_house_slug})


def menu_edit(request, coffee_house_slug, menu_slug):
    """Редактировать меню"""
    menu = queries.get_object_by_slug(Menu, menu_slug)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            menu.save()
            return redirect('menu:menu_details',
                            coffee_house_slug=coffee_house_slug,
                            menu_slug=menu.slug)
    else:
        form = MenuForm(instance=menu)
    return render(request, 'service/edit.html',
                  {'form': form})


def menu_delete(request, coffee_house_slug, menu_slug):
    queries.delete_object_by_slug(Menu, menu_slug)
    return redirect('cafe:coffee_house_details', coffee_house_slug=coffee_house_slug)


# Блок позиций
def menu_item_details(request, coffee_house_slug, menu_slug, item_id):
    """Подробнее о позиции"""
    item = queries.get_object_by_pk(MenuItem, item_id)
    return render(request, 'menu/item/details.html',
                  {'item': item,
                   'coffee_house_slug': coffee_house_slug,
                   'menu_slug': menu_slug})


def menu_item_add(request, coffee_house_slug, menu_slug):
    """Добавить позицию"""
    if request.method == 'POST':
        form = MenuItemForm(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            item.menu_id = queries.get_object_by_slug(Menu, menu_slug).id
            item.save()
            return redirect('menu:menu_details',
                            coffee_house_slug=coffee_house_slug,
                            menu_slug=menu_slug)
    else:
        form = MenuItemForm()
    return render(request, 'menu/item/add.html',
                  {'form': form,
                   'coffee_house_slug': coffee_house_slug,
                   'menu_slug': menu_slug})


def menu_item_edit(request, coffee_house_slug, menu_slug, item_id):
    """Редактировать позицию"""
    item = queries.get_object_by_pk(MenuItem, item_id)
    if request.method == 'POST':
        form = MenuItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()
            item.save()
            return redirect('menu:menu_item_details',
                            coffee_house_slug=coffee_house_slug,
                            menu_slug=menu_slug,
                            item_id=item.id)
    else:
        form = MenuItemForm(instance=item)
    return render(request, 'service/edit.html',
                  {'form': form})


def menu_item_delete(request, coffee_house_slug, menu_slug, item_id):
    item = queries.delete_object_by_pk(MenuItem, item_id)
    return redirect('menu:menu_details',
                    coffee_house_slug=coffee_house_slug,
                    menu_slug=menu_slug)
