from django import forms
from .models import UploadFile
class InputFileForm(forms.ModelForm):
    class Meta:
        model = UploadFile
        fields = ['uploaded_file']
        labels = {
            'uploaded_file':'Enter file here',
        }