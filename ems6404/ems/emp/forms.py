# forms.py
from django import forms
from .models import Complaint

class ComplaintForm(forms.ModelForm):
    class Meta:
        model = Complaint
        fields = ['complaint_text', 'employee_id']
        widgets = {
            'complaint_text': forms.Textarea(attrs={
                'class': 'input-field',
                'rows': 4,
                'placeholder': 'Describe your issue...'
            }),
            'employee_id': forms.TextInput(attrs={
                'class': 'input-field',
                'placeholder': 'Your Employee ID'
            })
        }


        
