from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [

    path('get/',views.getproduct),
    path('get/<id>',views.get_particular_product)
    # ... the rest of your URLconf goes here ...
]
