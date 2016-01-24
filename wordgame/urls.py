from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name= 'index'),
	url(r'^login/$', views.login, name = 'login'),
	url(r'^logout/$', views.logout, name = 'logout'),
	url(r'^game/$', views.game, name = 'game'),
	url(r'^game/load_q/$', views.load_q, name = 'load_q'),
]