from django.shortcuts import render, redirect, get_object_or_404
from .models import Menu, MenuItem
from .forms import MenuForm, MenuItemForm
from cafe.models import CoffeeHouse


# Блок меню
def menu_details(request, coffee_house_slug, menu_slug):
    """Подробнее о меню"""
    menu = get_object_or_404(Menu, slug=menu_slug)
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
    menu = get_object_or_404(Menu, slug=menu_slug)
    if request.method == 'POST':
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            menu = form.save()
            menu.save()
            return redirect('menu:menu_item_details',
                            coffee_house_slug=coffee_house_slug,
                            menu_slug=menu.slug)
    else:
        form = MenuForm(instance=menu)
    return render(request, 'service/edit.html',
                  {'form': form})


def menu_delete(request, coffee_house_slug, menu_slug):
    menu = get_object_or_404(Menu, slug=menu_slug)
    menu.delete()
    return redirect('cafe:coffee_house_details', coffee_house_slug=coffee_house_slug)


# Блок позиций
def menu_item_details(request, coffee_house_slug, menu_slug, item_id):
    """Подробнее о позиции"""
    item = get_object_or_404(MenuItem, pk=item_id)
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
            item.menu_id = Menu.objects.get(
                slug=menu_slug).id
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
    item = get_object_or_404(MenuItem, pk=item_id)
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
    item = get_object_or_404(MenuItem, pk=item_id)
    item.delete()
    return redirect('menu:menu_details',
                    coffee_house_slug=coffee_house_slug,
                    menu_slug=menu_slug)
