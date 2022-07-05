from django.db import models

# Create your models here.

class Timestamped(models.Model):

    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

class Post(Timestamped):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    text = models.TextField()

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.text} - {self.author.username}"