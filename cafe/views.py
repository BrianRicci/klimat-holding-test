from django.shortcuts import render, redirect, get_object_or_404
from .models import CoffeeHouse
from .forms import CoffeeHouseForm


def coffee_house_list(request):
    """Список кофеен"""
    coffee_houses = CoffeeHouse.objects.all()
    return render(request, 'cafe/list.html',
                  {'coffee_houses': coffee_houses})


def coffee_house_details(request, coffee_house_slug):
    """Подробнее о кофейне"""
    coffee_house = get_object_or_404(CoffeeHouse, slug=coffee_house_slug)
    return render(request, 'cafe/details.html',
                  {'coffee_house': coffee_house})


def coffee_house_add(request):
    """Добавить кофейню"""
    if request.method == 'POST':
        form = CoffeeHouseForm(request.POST)
        if form.is_valid():
            coffee_house = form.save()
            coffee_house.save()
            return redirect('cafe:coffee_house_list')
    else:
        form = CoffeeHouseForm()
    return render(request, 'cafe/add.html',
                  {'form': form})


def coffee_house_edit(request, coffee_house_slug):
    """Редактировать кофейню"""
    coffee_house = get_object_or_404(CoffeeHouse, slug=coffee_house_slug)
    if request.method == 'POST':
        form = CoffeeHouseForm(request.POST, instance=coffee_house)
        if form.is_valid():
            coffee_house = form.save()
            coffee_house.save()
            return redirect('cafe:coffee_house_details', coffee_house_slug=coffee_house.slug)
    else:
        form = CoffeeHouseForm(instance=coffee_house)
    return render(request, 'cafe/edit.html',
                  {'form': form})
