from django.db import models
from django.template.defaultfilters import slugify


class CoffeeHouses(models.Model):
    """Кофейни"""
    name = models.CharField(max_length=64, unique=True)
    slug = models.SlugField(max_length=128, unique=True)
    # Название и слаг уникальные, потому что слаг будет использоваться в ссылках
    work_time = models.CharField(max_length=128)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        ordering = ['-created']

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs):
        if self.name:
            self.slug = slugify(self.name)

        super(CoffeeHouses, self).save(*args, **kwargs)
