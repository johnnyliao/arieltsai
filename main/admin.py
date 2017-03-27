#-*- encoding: utf-8 -*-
from django import forms

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin, UserChangeForm as DjangoUserChangeForm
from django.contrib.auth.forms import UserCreationForm as DjangoUserCreationForm
from main.models import Action, VideoLink
from salmonella.admin import SalmonellaMixin

class ActionAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["name", "email", "phone"]
    search_fields = ["name"]

class VideoLinkAdmin(SalmonellaMixin, admin.ModelAdmin):
    list_display = ["link", "image_tag", "count"]
    search_fields = ["link"]


admin.site.register(Action, ActionAdmin)
admin.site.register(VideoLink, VideoLinkAdmin)
