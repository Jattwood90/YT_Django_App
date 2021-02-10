from .models import YT
from django import forms

class YTForm(forms.ModelForm):
	class Meta:
		model = YT
		fields = ['url', 'video']
		labels = {'url':'YouTube URL', 'video':'Channel ID'}

class SearchForm(forms.Form):
	search_term = forms.CharField(max_length=255, label='Search for Videos:')
	video = YT.video
