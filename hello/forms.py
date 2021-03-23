from django import forms
from .models import Friend

class FriendForm( forms.ModelForm ):
  class Meta:
    model = Friend
    fields = ['name', 'mail', 'gender', 'age', 'birthday']

class FindForm( forms.Form ):
  find = forms.CharField( label = 'Find', required = False )

# class CheckForm( forms.Form ):
#   required = forms.IntegerField(label = 'Required')
#   empty = forms.CharField(label='Empty', empty_value = True)
#   min = forms.IntegerField(label = 'Min', min_value = 10)
#   max = forms.IntegerField(label = 'Max', max_value = 10)
  
# class CheckForm( forms.Form ):
#   date = forms.DateField(label = 'Date', input_formats = ['%d'])
#   time = forms.TimeField(label = 'Time')
#   datetime = forms.DateTimeField(label = 'DateTime')

class CheckForm( forms.Form ):
  str = forms.CharField(label = 'String')
  
  def clean( self ):
    cleaned_data = super().clean()
    str = cleaned_data['str']
    if( str.lower().startswith('no')):
      raise forms.ValidationError("you input 'NO!'")