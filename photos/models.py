from django.db import models

# Create your models here.

class Gallery(models.Model):
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to="gallercovers/%Y/%m/%d/")



    def __repr__(self):
        return self.title




