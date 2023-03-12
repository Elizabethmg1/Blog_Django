from .models import page
from django.forms import ModelForm

class pageFormulario(ModelForm):
    class Meta:
        model = page
        fields = "__all__"
