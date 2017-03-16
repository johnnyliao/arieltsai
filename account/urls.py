
from rest_framework.urlpatterns import format_suffix_patterns

from django.conf.urls import patterns, url
from django.conf.urls.defaults import patterns, include, url
from account.views import *

urlpatterns = format_suffix_patterns(patterns('',
	(r'^', include('allauth.urls')),
))