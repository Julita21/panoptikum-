from django.test import TestCase

from relations.models import Author


class AuthorTest(TestCase):

    def create_author(self, name="Arnold", last_name="Jacobs"):
        return Author.objects.create(name=name, last_name=last_name)

    def test_author_created(self):
        a = self.create_author()
        self.assertTrue(isinstance(a, Author))
        self.assertEqual(str(a), "Arnold Jacobs")