from django.contrib import admin

from .models import Categoria
from .models import Post

class CategoriaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class PostAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    
# Register your models here.

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Post, PostAdmin)
