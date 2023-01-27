from django.contrib import admin

# Register your models here.
from .models import productMainModel,productImageModel, productColourModel

admin.site.register(productMainModel)
admin.site.register(productImageModel)
admin.site.register(productColourModel)

