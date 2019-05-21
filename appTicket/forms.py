from django import forms
from appTicket.models import Banda, GrupoBandas

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ["nome", "email", "genero", "independente"]

class GrupoBandasForm(forms.ModelForm):
    class Meta:
        model = GrupoBandas
        fields = ["nome", "genero", "data", "estado", "biografia", "foto"]