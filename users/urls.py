from django.urls import path
from . import views


urlpatterns = [
    path('users/', views.UsuarioList.as_view()),
    path('users/<int:pk>/', views.UsuarioDetail.as_view()),
]
