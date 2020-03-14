# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class User(models.Model):
    """
    Represents an user belonging to the organistaion
    """
    user = models.OneToOneField(user, null=False, blank=False, on_delete=models.CASCADE, related_name='user')
    name = models.CharField(max_length=255, null=True, blank=False)
    email = models.EmailField(null=True, blank=False)
    is_admin=models.BooleanField(null=False, blank=False, default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "%s" % (self.user)