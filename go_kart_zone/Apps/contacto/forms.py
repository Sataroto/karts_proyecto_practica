from django import forms
# Create your models here.
class FormularioContacto(forms.Form):
    nombre = forms.CharField( max_length = 50, required = True, label='Nombre')
    email = forms.EmailField(label = 'Email', required=True)
    contenido = forms.CharField(label='Contenido', widget=forms.Textarea )