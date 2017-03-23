
from django.conf.urls import patterns, url
from main.views import JoinActionView, index

urlpatterns = patterns(".views",
	url('^index/', index),
	url('^join_action/', JoinActionView.as_view()),

)
