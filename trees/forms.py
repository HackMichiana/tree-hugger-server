from django.forms import ModelForm
from .models import Tree, Image

class TreeForm(ModelForm):
    class Meta:
        model = Tree
