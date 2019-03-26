# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Candidate(models.Model):

    STARS = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5 - Good'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10 - God')
    )

    BEFORE = (
        (1, 'Not for us'),
        (2, 'Interesting'),
        (3, 'Fantastic'),
    )

    AFTER = (
        (1, 'Not for us'),
        (2, 'Short list'),
        (3, 'Hire'),
    )

    name = models.CharField(max_length=128)
    role = models.ForeignKey('roles.Role', on_delete=models.CASCADE)
    interview_date = models.DateTimeField(null=True, blank=True)
    impressions_before = models.IntegerField(choices=BEFORE, null=True, blank=True)
    impressions_after = models.IntegerField(choices=AFTER, null=True, blank=True)

    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    tech_skills = models.IntegerField(choices=STARS, null=True, blank=True)
    soft_skills = models.IntegerField(choices=STARS, null=True, blank=True)

    notes = models.TextField(null=True, blank=True)
    cv = models.FileField(null=True, blank=True)
    salary = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
