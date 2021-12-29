from django import forms
from .models import *

class AddContactForm(forms.ModelForm):
        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['create_data'].disabled = True
            self.fields['edit_data'].disabled = True

        class Meta:
            model = Contact
            fields = ['last_name',
                      'name',
                      'middle_name',
                      'mobile_phone',
                      'work_phone',
                      'organization',
                      'e_mail',
                      'info',
                      'create_data',
                      'edit_data',
                      ]
            widgets = {
                'organization': forms.Textarea(attrs={'cols':60, 'rows':2}),
                'info': forms.Textarea(attrs={'cols': 60, 'rows': 5})
            }





