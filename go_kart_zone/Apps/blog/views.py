from django.shortcuts import render
from .models import Post
from .models import Categoria

# Create your views here.
def blog(request):

    categorias = Categoria.objects.all()
     
    posts = reversed(Post.objects.all())

    return render(request, "blog/blog.html", {'posts' : posts , 'categorias': categorias})

def categorias(request, categoria_id):
    categoria = Categoria.objects.get(id = categoria_id)
    posts = reversed(Post.objects.filter(categorias = categoria))

    return render(request, "blog/categorias.html", {'posts': posts, 'categorias' : Categoria.objects.all()})