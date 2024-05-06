from django.contrib import admin
from django.urls import path, re_path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('account.urls', namespace='account')),

    path('', include('cafe.urls', namespace='cafe')),
    path('<slug:coffee_house_slug>/menu/',
         include('menu.urls', namespace='menu')),

    # api urls
    path('api/v1/', include('api.urls', namespace='api')),
    path('api/v1/auth/', include('djoser.urls')),
    re_path(r'^auth/', include('djoser.urls.authtoken')),
]
