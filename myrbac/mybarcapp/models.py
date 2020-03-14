# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User as user
from django.db.models.signals import post_save,pre_save
# Create your models here.
class User(models.Model):
    """
    Represents an user
    """
    user = models.OneToOneField(user, null=False, blank=False, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % (self.user)

    def create_user(sender, instance, created, **kwargs):
        """
        create a user when a django  user is created
        """
        user, created = User.objects.get_or_create(user=instance)
        user.name = instance.first_name
        user.email = instance.email
        user.save()

    post_save.connect(create_user, sender=user)


class Resource(models.Model):
    resource = models.CharField(max_length=255, null=False,unique=True)

    def __str__(self):
        return self.resource

class Role(models.Model):
    resource = models.ForeignKey(Resource, related_name='rm')
    name = models.CharField(max_length=128, null=False, blank=False)
    users = models.ManyToManyField(User,blank=True)
    ACTION_TYPE=(
        ('Read','read'),
        ('Write','write'),
        ('Delete','delete'),
    )
    action_type = models.CharField(max_length=255, null=False, blank=False, choices=ACTION_TYPE,default='Read')

    def __str__(self):
        return self.name

