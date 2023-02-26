from django.test import TestCase
from django.urls import reverse

from books.models import Book, BookReview
from users.models import CustomUser


class HomePgaeTestCase(TestCase):
    def test_paginated_list(self):
        book = Book.objects.create(title="Book1", description="Description1", isbn="123121")
        user = CustomUser.objects.create(
            username="jahongir",
            first_name="Jahongir", email=""
        )

        user.set_password("somepass")
        user.save()
        review1 = BookReview.objects.create(book=book, user=user, stars_given=3, comment="It's verry good book you should buy this book")
        review2 = BookReview.objects.create(book=book, user=user, stars_given=4, comment="Lorem ipsum dolor set should python manage.py ")
        review3 = BookReview.objects.create(book=book, user=user, stars_given=5, comment="This is very nice book ")

        response = self.client.get(reverse("home_page") + "?page_size=2")

        self.assertContains(response, review3.comment)
        self.assertContains(response, review2.comment)
        self.assertNotContains(response, review1.comment)