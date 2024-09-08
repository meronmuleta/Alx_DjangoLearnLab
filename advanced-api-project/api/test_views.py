from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from .models import Book, Author

class BookAPITests(APITestCase):

    def setUp(self):
        # Setting up a user and author
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.author = Author.objects.create(name='John Doe')

        # Log in the user
        self.client.login(username='testuser', password='testpassword')

        # Setting up initial data
        self.book = Book.objects.create(title='Test Book', publication_year=2020, author=self.author)

    def test_create_book(self):
        url = reverse('book-create')
        data = {'title': 'New Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_retrieve_book_list(self):
        url = reverse('book-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure the initial setup book is there

    def test_update_book(self):
        url = reverse('book-update', kwargs={'pk': self.book.pk})
        data = {'title': 'Updated Book', 'publication_year': 2022, 'author': self.author.id}
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book')

    def test_delete_book(self):
        url = reverse('book-delete', kwargs={'pk': self.book.pk})
        response = self.client.delete(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_filter_books(self):
        url = reverse('book-list')
        response = self.client.get(url + '?publication_year=2020', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['publication_year'], 2020)

    def test_search_books(self):
        url = reverse('book-list')
        response = self.client.get(url + '?search=Test', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_order_books(self):
        url = reverse('book-list')
        response = self.client.get(url + '?ordering=-publication_year', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], 'Test Book')

    def test_permissions(self):
        self.client.logout()  # Testing without authentication
        url = reverse('book-create')
        data = {'title': 'Unauthorized Book', 'publication_year': 2021, 'author': self.author.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

