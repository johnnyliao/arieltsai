
from django.conf.urls import patterns, url
from main.views import index

urlpatterns = patterns(".views",
	url('^index/', index),

)
