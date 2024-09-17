from django.forms import ModelForm
from main.models import ObjectEntry

class ModelObjectForm(ModelForm):
    class Meta:
        model = ObjectEntry
        fields = ["name", "price", "description"]