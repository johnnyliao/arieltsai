#-*- encoding: utf-8 -*-

from django.contrib.auth.models import AbstractUser

from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils import timezone

from django.contrib.contenttypes import generic
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.sites.models import Site

import urlparse, settings

from django.utils import simplejson
from allauth.socialaccount.models import SocialAccount
from mezzanine.utils.models import AdminThumbMixin

class User(AbstractUser, AdminThumbMixin):

	def __unicode__(self):
		return self.username

	def save(self, *args, **kwargs):
		super(User, self).save(*args, **kwargs)



