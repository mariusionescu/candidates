# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Candidate(models.Model):

    BEFORE = (
        ('before_1', 'Not okay'),
        ('before_2', 'Rather not'),
        ('before_2', 'Interesting'),
        ('before_3', 'We must meet')
    )

    AFTER = (
        ('after_1', 'It is a no'),
        ('after_2', 'Rather not'),
        ('after_3', 'Short list'),
        ('after_4', 'Make an offer'),
    )
    name = models.CharField(max_length=128)
    role = models.ForeignKey('roles.Role', on_delete=models.CASCADE)
    interview_date = models.DateTimeField(null=True, blank=True)
    impressions_before = models.CharField(max_length=32, choices=BEFORE, null=True, blank=True)
    impressions_after = models.CharField(max_length=32, choices=AFTER, null=True, blank=True)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    tech_skills = models.IntegerField(default=0, null=True, blank=True)
    soft_skills = models.IntegerField(default=0, null=True, blank=True)

    notes = models.TextField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
