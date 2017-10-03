# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from apps.posts.models import Post


admin.site.register(Post)
