from django.conf.urls import url
from . import views


urlpatterns = [
	url(r'^$', views.index, name= 'index'),
	url(r'^login/$', views.LoginView.as_view(),name = 'login'),
	url(r'^logout/$', views.logout ,name = 'logout'),
	url(r'^game/$', views.game, name = 'game'),
	url(r'^game/load_q/$', views.load_q, name = 'load_q'),
	url(r'^game/check_ans/$', views.check_ans, name = 'check_ans'),
	url(r'^([a-zA-Z]{1,18})$', views.profile.as_view(), name = 'profile'),
]