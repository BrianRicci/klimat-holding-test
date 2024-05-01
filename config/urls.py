from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),
    path('api/v1/', include('api.urls', namespace='api')),


    path('', include('cafe.urls', namespace='cafe')),
    path('<slug:coffee_house_slug>/menu/',
         include('menu.urls', namespace='menu')),
]
