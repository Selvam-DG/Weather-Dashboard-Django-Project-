from django import forms

class WeatherForm(forms.Form):
    location = forms.CharField(label='Enter City', max_length=100)
    days = forms.IntegerField(label='Days', min_value=1, max_value=10, initial=7)
