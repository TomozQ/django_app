from django import forms

class HelloForm(forms.Form):
  data = [
    ('one', 'radio 1'),
    ('two', 'radio 2'),
    ('three', 'radio 3'),
    ('four', 'radio 4'),
    ('five', 'radio 5'),
  ]

  choice = forms.MultipleChoiceField(label='radio', choices=data, widget=forms.SelectMultiple(attrs={'size': 6}))