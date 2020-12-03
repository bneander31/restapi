from django import forms

from .models import Update as UpdateModel

class UpdateModelForm(forms.UpdateModelForm):
    class Meta:
        model = UpdateModel
        fields = [
            'user',
            'content',
            'image'
        ]