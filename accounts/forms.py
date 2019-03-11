from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput)
	email = forms.EmailField(required=True)
	class Meta:
		model = User
		fields = [
					'username',
					'email',
					'password'
				]