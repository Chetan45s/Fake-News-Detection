from django import forms

LABEL_CHOICES = (
    ('0', 'Fake News'),
    ('1', 'Real News')
)

class InputForm(forms.Form):
    text = forms.CharField(required=False)
    title = forms.CharField(required=False)
    text_cont = forms.CharField(required=False)
    title_cont = forms.CharField(required=False)
    label = forms.ChoiceField(widget=forms.RadioSelect, choices=LABEL_CHOICES)