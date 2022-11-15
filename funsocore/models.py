from django.db import models
from django.contrib.auth.models import User

# Create your models here.
STATUS = (
    (0,"Borrador"),
    (1,"Publicado")
)

class Post(models.Model):
    titulo = models.CharField(max_length=200, unique=True)
    subtitulo = models.SlugField(max_length=200, unique=True)
    autor = models.ForeignKey(User, on_delete= models.CASCADE,related_name='blog_posts')
    fecha_actualizacion = models.DateTimeField(auto_now= True)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    estado = models.IntegerField(choices=STATUS, default=0)
    foto = models.ImageField(upload_to = "posts", null=True)
    class Meta:
        ordering = ['-fecha_creacion']

    def __str__(self):
        return self.title