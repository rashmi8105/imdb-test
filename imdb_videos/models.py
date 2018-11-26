# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class Videos(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=100, blank=True, default='')
    genre = models.TextField()
    popularity = models.CharField(max_length=100, default='')
    director = models.CharField(max_length=100, blank=True, default='')
    imdb_score = models.CharField(default='0.0', max_length=100)

    class Meta:
        ordering = ('created',)
