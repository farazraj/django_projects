from django.forms import ModelForm
from lost.models import Crud

class updaterecordform(ModelForm):
    class Meta:
        model = Crud
        fields = '__all__'
