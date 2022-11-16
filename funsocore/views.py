from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from . import models
# Create your views here.

def post_lista(request):
    posts = models.Post.objects.filter(state__exact=1)
    #posts = models.Post.objects.all()
    context = {'posts': posts}
    return render(request, 'blogs/blog_list.html', context)

def post_detalle(request, pk):
    post = get_object_or_404(models.Post, pk=pk)
    context = {'post': post}
    return render(request, 'blogs/blog_detalle.html', context)

