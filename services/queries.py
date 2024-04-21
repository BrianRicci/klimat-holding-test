from django.db import models
from django import forms
from django.shortcuts import get_object_or_404


def get_all_objects(model: models.Model):
    """Запрос на вывод всех записей"""
    return model.objects.all()


def get_object_by_slug(model: models.Model, slug):
    """Запрос на вывод одной записи по slug"""
    return get_object_or_404(model, slug=slug)


def get_object_by_pk(model: models.Model, pk):
    """Запрос на вывод одной записи по первичному ключу"""
    return get_object_or_404(model, pk=pk)


def delete_object_by_slug(model: models.Model, slug) -> None:
    """Удаление записи по slug"""
    object = get_object_by_slug(model, slug)
    object.delete()


def delete_object_by_pk(model: models.Model, pk) -> None:
    """Удаление записи по первичному ключу"""
    object = get_object_by_pk(model, pk)
    object.delete()
