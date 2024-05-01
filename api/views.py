from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser

from cafe.models import CoffeeHouse
from .serializers import CoffeeHouseSerializer
from menu.models import Menu, MenuItem
from .serializers import MenuSerializer, MenuItemSerializer
from .permissions import IsAdminOrReadOnly, IsOwnerOrReadOnly


class CoffeeHouseAPIList(generics.ListCreateAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )


class CoffeeHouseAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = (IsOwnerOrReadOnly, )


class CoffeeHouseAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = CoffeeHouse.objects.all()
    serializer_class = CoffeeHouseSerializer
    permission_classes = (IsAdminOrReadOnly, )

#################################################


class MenuAPIList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer


class MenuAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

#################################################


class MenuItemAPIList(generics.ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer


class MenuItemAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer
