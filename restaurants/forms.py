from django import forms
from restaurants.models import Review

class ReviewForm(forms.ModelForm):
	star_count = forms.IntegerField(label="", required=True)
	description = forms.CharField(widget=forms.Textarea(attrs={'rows': 4, 
															   'cols': 50,
															   'placeholder':'Help other foodies by sharing your review'
																}), required=True, label="")
	class Meta:
		model = Review
		fields = [
					'star_count',
					'description'
				]