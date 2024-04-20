from django.db import models
from django.template.defaultfilters import slugify


class Menus(models.Model):
    """Меню кофейни"""
    coffee_house = models.ForeignKey('cafe.CoffeeHouses',
                                     on_delete=models.CASCADE,
                                     related_name='menu')
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)

    class Meta:
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)

        super(Menus, self).save(*args, **kwargs)


class MenuItems(models.Model):
    """Одна из позиций в меню"""

    class MeasureUnit(models.TextChoices):
        """Единицы измерений"""
        G = 'г', 'Грамм'
        KG = 'кг', 'Килограмм'
        ML = 'мл', 'Миллилитр'
        L = 'л', 'Литр'

    menu = models.ForeignKey('Menus',
                             on_delete=models.CASCADE,
                             related_name='item')
    name = models.CharField(max_length=64)
    size = models.IntegerField()
    measure_unit = models.CharField(max_length=2,
                                    choices=MeasureUnit.choices)

    class Meta:
        ordering = ['-name']

    def __str__(self) -> str:
        return self.name
