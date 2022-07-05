from unittest import TestCase

from django.urls import reverse

from relations.models import Author


class AuthorTest(TestCase):

    def create_author(self, name="Arnold", last_name= "Jacobs"):
        return Author.objects.create(name=name, last_name=last_name)

    def test_author_details_view(self):
        a = self.create_author()
        url = reverse("publications:author_details", args=[a.id])
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.name, resp.content.decode())

    def test_author_list_view_with_q(self):
        a = self.create_author()
        url = reverse("publications:author_list")
        url += "?q=xxxxxx"
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertNotIn(a.name, resp.content.decode())

    def test_author_list_view(self):
        a = self.create_author()
        url = reverse("publications:authors_list")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
        self.assertIn(a.name, resp.content.decode())
