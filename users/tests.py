from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Usuario

class UsuarioAPITests(APITestCase):
    url = '/api/v1/users/'

    def setUp(self):
        self.auth_user = User.objects.create_user(
            username='testuser', password='testpassword123'
        )
        self.client.force_authenticate(user=self.auth_user)

        self.usuario = Usuario.objects.create(
            nombre="juan",
            apellido="perez",
            edad=40
        )

    def test_list_users(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], self.usuario.nombre)

    def test_create_user(self):
        data = {
            "nombre": "ana",
            "apellido": "gomez",
            "edad": 35
        }
        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Usuario.objects.count(), 2)
        self.assertEqual(response.data['nombre'], "ana")

    def test_get_single_user(self):
        url_with_id = f'{self.url}{self.usuario.id}/'
        response = self.client.get(url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.usuario.nombre)

    def test_update_user_put(self):
        url_with_id = f'{self.url}{self.usuario.id}/'
        data = {
            "nombre": "Juan Carlos",
            "apellido": "Bodoque",
            "edad": 41
        }
        response = self.client.put(url_with_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.usuario.refresh_from_db()
        self.assertEqual(self.usuario.nombre, "Juan Carlos")

    def test_update_user_patch(self):
        url_with_id = f'{self.url}{self.usuario.id}/'
        data = {"activo": False}
        response = self.client.patch(url_with_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.usuario.refresh_from_db()
        self.assertFalse(self.usuario.activo)

    def test_delete_user(self):
        url_with_id = f'{self.url}{self.usuario.id}/'
        response = self.client.delete(url_with_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Usuario.objects.filter(id=self.usuario.id).exists())

    def test_unauthenticated_request(self):
        from rest_framework.test import APIClient
        unauthenticated_client = APIClient()
        
        response = unauthenticated_client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
