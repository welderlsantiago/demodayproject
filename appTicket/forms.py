from django import forms
from appTicket.models import Banda

class BandaForm(forms.ModelForm):
    class Meta:
        model = Banda
        fields = ["nome", "email", "genero", "independente"]