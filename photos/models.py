from django.db import models

# Create your models here.
from django_extensions import auth


class Gallery(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()


    def __repr__(self):
        return self.title




