from rest_framework import serializers
from .models import productMainModel,productColourModel,productImageModel



class productColourModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productColourModel
        fields=('__all__')
class productImageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model=productImageModel
        fields=('__all__')

class productMainModelSerializer(serializers.ModelSerializer):
    product_image = productImageModelSerializer(many=True,read_only=True)
    uploaded_images = serializers.ListField(
        child = serializers.FileField(max_length = 1000000, allow_empty_file = False, use_url = False),
        write_only = True)
    product_color = productColourModelSerializer(many=True,read_only=True)   
    class Meta:
        model=productMainModel
        fields=['Title','Price','product_image','product_color','uploaded_images']
        extra_kwargs = {"user":{"read_only":True}}

    def create(self, validated_data):
        uploaded_data = validated_data.pop('uploaded_images')
        new_product =  productMainModel.objects.create(**validated_data)
        for uploaded_item in uploaded_data:
            new_product_image = productImageModel.objects.create(Product = new_product, Image = uploaded_item)
        return new_product
     