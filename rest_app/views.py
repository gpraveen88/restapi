
# Create your views here.
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import productMainModel,productColourModel,productImageModel
from .serializers import productMainModelSerializer,productColourModelSerializer,productImageModelSerializer

# Create your views here.
@api_view(['GET'])
def getproduct(request):
    product_data = productMainModel.objects.all()
    serializer = productMainModelSerializer(product_data, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_particular_product(request,id):
    product_data = productMainModel.objects.get(id=id)
    serializer = productMainModelSerializer(product_data)
    return Response(serializer.data)