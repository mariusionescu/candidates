# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from candidates.models import Candidate


class CandidateAdmin(admin.ModelAdmin):

    readonly_fields = ('user',)

    def get_queryset(self, request):
        queryset = super(CandidateAdmin, self).get_queryset(request)
        if request.user.is_superuser:
            return queryset
        else:
            return queryset.filter(user=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.pk:
            obj.user = request.user
        return super(CandidateAdmin, self).save_model(request, obj, form, change)


admin.site.register(Candidate, CandidateAdmin)
