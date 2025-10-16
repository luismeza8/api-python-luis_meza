from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from products.models import Producto
from products.serializer import ProductoSerializer


class ProductList(APIView):
    def get(self, _):
        products = Producto.objects.all()
        serializer = ProductoSerializer(products, many=True)
        
        return Response(serializer.data)


    def post(self, request):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ProductDetail(APIView):
    def get(self, _, pk):
        product = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(product)

        return Response(serializer.data)

    def put(self, request, pk):
        product = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(product, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    # agregue este metodo adicional en caso de que se quiera editar solo una parte del producto
    # por ejemplo cuando solo se quiere cambiar el estado del producto
    def patch(self, request, pk):
        product = get_object_or_404(Producto, pk=pk)
        serializer = ProductoSerializer(product, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


    def delete(self, _, pk):
        product = get_object_or_404(Producto, pk=pk)
        product.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

