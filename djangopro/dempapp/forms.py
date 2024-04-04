from django import forms
from .models import reviews_and_ratings

class ContactForm(forms.ModelForm):
    class Meta:
        model = reviews_and_ratings
        fields = ['review']

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['review'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Enter your review'})
