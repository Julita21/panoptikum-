from django.db import models

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name} {self.last_name}"


class AuthorBiogram(models.Model):
    # one to one relation
    author = models.OneToOneField(Author, on_delete=models.CASCADE)
    bio = models.TextField()


class Tag(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self): return self.name

class Publication(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='publications')
    title = models.CharField(max_length=200)
    year = models.IntegerField()
    # relacja m2m
    tags = models.ManyToManyField(Tag, related_name='publications')