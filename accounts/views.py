from django.shortcuts import render, redirect
from accounts.forms import UserRegistrationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import (
		authenticate,
		login,
		logout,
	)

def registration_view(request):
	form = UserRegistrationForm(request.POST or None)
	if form.is_valid():
		user = form.save(commit=False)
		password = form.cleaned_data.get('password')
		user.set_password(password)
		user.save()
		new_user = authenticate(username=user.username, password=password)
		login(request, new_user)
		return redirect('register')

	context = {
		"form":form
	}
	return render(request, "register.html", context)

def logout_view(request):
	logout(request)
	return redirect('landing')

@login_required
def landing_view(request):
	return render(request, 'landing.html', {})