from rest_framework import serializers
from cafe.models import CoffeeHouse
from menu.models import Menu, MenuItem


class CoffeeHouseSerializer(serializers.ModelSerializer):
    """Сериализатор кофейни"""

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    menus = serializers.SerializerMethodField()

    class Meta:
        model = CoffeeHouse
        fields = ['id', 'name', 'slug', 'work_time',
                  'created', 'description', 'menus', 'user']
        read_only_fields = ['slug', 'created']

    def get_menus(self, obj):
        queryset = Menu.objects.filter(coffee_house=obj)
        return [MenuSerializer(q).data for q in queryset]


class MenuSerializer(serializers.ModelSerializer):
    """Сериализатор меню"""

    menu_items = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ['id', 'coffee_house_id', 'slug', 'name', 'menu_items']
        read_only_fields = ['slug']

    def get_menu_items(self, obj):
        queryset = MenuItem.objects.filter(menu=obj)
        return [MenuItemSerializer(q).data for q in queryset]


class MenuItemSerializer(serializers.ModelSerializer):
    """Сериализатор позиций"""

    class Meta:
        model = MenuItem
        fields = ['id', 'menu_id', 'name']
