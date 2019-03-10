"""rrs_admin URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView
from accounts.views import (
	registration_view,
	logout_view,
	landing_view,
)
from restaurants.views import restaurant_details


urlpatterns = [
	url(r'^$', landing_view, name="landing"),
	url(r'^register/', registration_view, name="register"),
	url(r'^login/$', LoginView.as_view(template_name="login.html"), name="login"),
	url(r'^logout/', logout_view, name="logout"),
    url(r'^restaurant/(?P<res_id>\d+)/$', restaurant_details, name="restaurant-details"),
    url(r'^admin/', admin.site.urls),
] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
