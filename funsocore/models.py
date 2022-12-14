from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.
STATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    occurr_date = models.DateTimeField(default=datetime.now)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    state = models.IntegerField(choices=STATUS, default=0)
    photo = models.ImageField(upload_to = "posts", null=True)
    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title