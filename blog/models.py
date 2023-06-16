from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    cover = models.FileField(upload_to="media/blog_covers")
    body = models.TextField()
    abstract = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
