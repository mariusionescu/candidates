# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from roles.models import Role, Company

admin.site.register(Role)
admin.site.register(Company)
