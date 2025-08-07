from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Product, Cart, CartItem

class CartAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.product = Product.objects.create(name="Test Product", price=50.00)

    def test_add_product_to_cart(self):
        response = self.client.post('/cart/', {
            'product_id': self.product.id,
            'quantity': 2
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(CartItem.objects.count(), 1)
        self.assertEqual(CartItem.objects.first().quantity, 2)

    def test_get_cart(self):
        # Add to cart first
        self.client.post('/cart/', {
            'product_id': self.product.id,
            'quantity': 3
        })
        # Retrieve cart
        response = self.client.get('/cart/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('items', response.data)
        self.assertEqual(len(response.data['items']), 1)
        self.assertEqual(response.data['items'][0]['quantity'], 3)
