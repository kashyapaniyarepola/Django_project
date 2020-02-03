# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class Post(models.Model):
    p_id = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    price = models.CharField(max_length=255)

        