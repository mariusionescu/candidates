# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Company(models.Model):

    class Meta:
        verbose_name_plural = "Companies"
        verbose_name = "Company"

    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(null=True, blank=True)
    company = models.ForeignKey('roles.Company', on_delete=models.CASCADE)

    users = models.ManyToManyField('auth.User')

    def __str__(self):
        return "{} - {}".format(self.company, self.name)

