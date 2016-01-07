from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^(?P<user_name>[a-zA-Z]+)/$', views.index, name= 'index'),
]