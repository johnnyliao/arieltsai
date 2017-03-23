#-*- encoding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes import generic

from django.contrib.auth.models import AbstractUser

from django.utils import timezone

from django.contrib.contenttypes import generic

from django.core.exceptions import ObjectDoesNotExist

from django.contrib.sites.models import Site
import urlparse, settings

#for facebook comment plugin record
class Action(models.Model):
    name = models.CharField(_(u"姓名"), max_length=100)
    phone = models.CharField(_(u"電話"), max_length=100)
    email = models.CharField(_(u"EMAIL"), max_length=100)

    class Meta:
        verbose_name = _(u'活動')
        verbose_name_plural = _(u'活動列表')



