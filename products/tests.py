from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from rest_framework import status

from .models import Producto


class ProductoAPITests(APITestCase):
    url = '/api/v1/products/'

    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser', password='testpassword123'
        )

        self.client.force_authenticate(user=self.user)

        self.product = Producto.objects.create(
            nombre='Celular',
            precio='15000.00',
            stock=10
        )


    def test_list_products(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['nombre'], self.product.nombre)


    def test_create_product(self):
        data = {
            'nombre': 'Botella',
            'precio': '100',
            'stock': 25
        }

        response = self.client.post(self.url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Producto.objects.count(), 2)
        self.assertEqual(response.data['nombre'], 'Botella')


    def test_get_single_product(self):
        url_with_id = f'{self.url}{self.product.id}/'
        response = self.client.get(url_with_id)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nombre'], self.product.nombre)


    def test_update_product_put(self):
        url_with_id = f'{self.url}{self.product.id}/'

        data = {
            "nombre": "Producto Actualizado",
            "precio": "125.00",
            "stock": 5
        }
        response = self.client.put(url_with_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.nombre, "Producto Actualizado")


    def test_update_product_patch(self):
        url_with_id = f'{self.url}{self.product.id}/'
        data = {"activo": False}
        response = self.client.patch(url_with_id, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertFalse(self.product.activo)

    def test_delete_product(self):
        url_with_id = f'{self.url}{self.product.id}/'
        response = self.client.delete(url_with_id)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Producto.objects.filter(id=self.product.id).exists())

    def test_unauthenticated_request(self):
        from rest_framework.test import APIClient
        unauthenticated_client = APIClient()
        
        response = unauthenticated_client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
