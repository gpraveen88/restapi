from rest_framework import serializers
from .models import productMainModel,productColourModel,productImageModel


class productMainModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields=('__all__')
class productColourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields=('__all__')
class productImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productMainModel
        fields=('__all__')
