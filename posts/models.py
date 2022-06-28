from django.db import models


from django.template.defaultfilters import slugify


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    content = models.TextField()

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __repr__(self):
        return f" {self.title} ({self.author})"


