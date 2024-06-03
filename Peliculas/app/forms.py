from django import forms
from .models import Pelicula

class PeliculaForm(forms.ModelForm):
    class Meta:
        model = Pelicula
        fields = ['titulo', 'sinopsis', 'duracion', 'genero']
        labels = {
            'titulo': 'Título',
            'sinopsis': 'Sinopsis',
            'duracion': 'Duración',
            'genero': 'Género'
        }
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'sinopsis': forms.Textarea(attrs={'class': 'form-control'}),
            'duracion': forms.NumberInput(attrs={'class': 'form-control'}),
            'genero': forms.TextInput(attrs={'class': 'form-control'})
        }
        
