
from django import forms

class ImageUploadForm(forms.Form):
    image = forms.ImageField(label="Select an image",
                             widget=forms.ClearableFileInput(attrs={
            'class': 'form-control-file',  # Add Bootstrap or custom class
            'style': 'color: white; font-weight: bold;'  # Inline styling (optional)
    })
    )
    
