# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from roles.models import Role, Company


class RoleAdmin(admin.ModelAdmin):

    def get_queryset(self, request):
        queryset = super(RoleAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(users=request.user)


admin.site.register(Role, RoleAdmin)
admin.site.register(Company)
