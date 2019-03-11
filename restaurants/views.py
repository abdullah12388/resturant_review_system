from django.shortcuts import render, redirect
from restaurants.forms import ReviewForm
from restaurants.models import Review
from django.contrib import messages
from rrs_admin import config
import requests
import json


def restaurant_details(request, res_id):
	form = ReviewForm(request.POST or None)
	if form.is_valid():
		star_count = form.cleaned_data.get('star_count')
		description = form.cleaned_data.get('description')
		reveiw, created = Review.objects.update_or_create(user = request.user, res_id = res_id,
													defaults = {
														'star_count': star_count,
														'description': description,
													}
												)
		if created:
			messages.success(request, 'Review Published Successfully')
		else:
			messages.success(request, 'Review Updated')
		return redirect('/restaurant/{0}'.format(str(res_id)))
	url = 'https://developers.zomato.com/api/v2.1/restaurant?res_id={0}'.format(str(res_id))
	header = {"User-agent": "curl/7.43.0", "Accept": "application/json", "user_key": "cd9ca69cad612fbd6b4cb9fe9d503906"}
	response = requests.get(url, headers=header)
	res_obj = response.json()
	context = {
		'res_data': res_obj,
		'form':form,
		"url":config.url
	}
	get_review(context, res_id)
	return render(request, 'restaurant.html', context)


def get_review(context, res_id):
	review_obj = Review.objects.filter(res_id=res_id)
	context['review_obj'] = review_obj
	return context