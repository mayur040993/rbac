# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import User, Role, Resource

admin.site.register(User)
admin.site.register(Role)
admin.site.register(Resource)