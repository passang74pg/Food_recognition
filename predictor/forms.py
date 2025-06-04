from django import forms
from .models import FoodPrediction

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = FoodPrediction
        fields = ['image']
        widgets = {
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control-file',
                'accept': 'image/*'
            })
        }