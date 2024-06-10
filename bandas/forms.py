from django import forms    # formulários Django
from .models import Banda, Album, Musica

class BandaForm(forms.ModelForm):
  class Meta:
    model = Banda        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Banda.

class AlbumForm(forms.ModelForm):
  class Meta:
    model = Album        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Album.

class MusicaForm(forms.ModelForm):
  class Meta:
    model = Musica        # classe para a qual é o formulário
    fields = '__all__'   # inclui no form todos os campos da classe Musica.