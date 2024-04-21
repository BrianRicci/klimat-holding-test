from django.db import models
from slugify import slugify


class Menu(models.Model):
    """Меню кофейни"""
    coffee_house = models.ForeignKey('cafe.CoffeeHouse',
                                     on_delete=models.CASCADE,
                                     related_name='menus')
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)

        super(Menu, self).save(*args, **kwargs)


class MenuItem(models.Model):
    """Одна из позиций в меню"""

    class MeasureUnit(models.TextChoices):
        """Единицы измерений"""
        G = 'г', 'Грамм'
        KG = 'кг', 'Килограмм'
        ML = 'мл', 'Миллилитр'
        L = 'л', 'Литр'

    menu = models.ForeignKey('Menu',
                             on_delete=models.CASCADE,
                             related_name='items')
    name = models.CharField(max_length=64)
    size = models.IntegerField()
    measure_unit = models.CharField(max_length=2,
                                    choices=MeasureUnit.choices)

    class Meta:
        ordering = ['name']

    def __str__(self) -> str:
        return self.name
