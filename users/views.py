from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Usuario
from .serializer import UsuarioSerializer


class UsuarioList(APIView):
    def get(self, _):
        users = Usuario.objects.all()
        serializer = UsuarioSerializer(users, many=True)

        return Response(serializer.data)


    def post(self, request):
        serializer = UsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class UsuarioDetail(APIView):
    def get(self, _, pk):
        user = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(user)

        return Response(serializer.data)


    def put(self, request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(user, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        user = get_object_or_404(Usuario, pk=pk)
        serializer = UsuarioSerializer(user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)


    def delete(self, _, pk):
        user = get_object_or_404(Usuario, pk=pk)
        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
