from .models import YT
from django import forms

class YTForm(forms.ModelForm):
	class Meta:
		model = YT
		fields = ['url']
		labels = {'url':'YouTube URL'}

class SearchForm(forms.Form):
	search_term = forms.CharField(max_length=255, label='Search for Videos:')