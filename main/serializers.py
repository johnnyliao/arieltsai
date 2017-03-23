#-*- encoding: utf-8 -*-

from django.utils.translation import ugettext_lazy as _
from main.models import Action

from rest_framework import serializers

from datetime import datetime,timedelta
from django.utils import timezone
import urlparse
from django.contrib.sites.models import Site

class ActionSerializer(serializers.ModelSerializer):

	class Meta:
		model = Action

