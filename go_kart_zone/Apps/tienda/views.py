from django.shortcuts import render

# Create your views here.
def tienda(request):
     
     return render(request, "tienda/tienda.html")

def categorias(request):
     
     return render(request, 'tienda/Categoria' )