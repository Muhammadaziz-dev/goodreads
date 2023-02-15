from django.test import TestCase
from django.urls import reverse

from books.models import Book


class BooksTestCase(TestCase):
    def test_no_books(self):
        response = self.client.get(reverse("books:list"))

        self.assertContains(response, "No books found")

    def test_books_list(self):
        Book.objects.create(title="Book1", description="Description1", isbn="123123")
        Book.objects.create(title="Book2", description="Description2", isbn="11111")
        Book.objects.create(title="Book3", description="Description3", isbn="2342423")

        response = self.client.get(reverse("books:list"))

        books = Book.objects.all()
        for book in books:
            self.assertContains(response, book.title)

    def test_detail_page(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="123123")

        response = self.client.get(reverse("books:detail", kwargs={"id": book.id}))

        self.assertContains(response, book.title)
        self.assertContains(response, book.description)