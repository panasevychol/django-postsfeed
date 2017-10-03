# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import json

from django.db import models

from apps.posts.constants import TITLE_MAX_LENGTH, BODY_MAX_LENGTH
from apps.users.models import User

class Post(models.Model):
    title = models.CharField(max_length=TITLE_MAX_LENGTH)
    body = models.CharField(max_length=BODY_MAX_LENGTH)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    approved = models.BooleanField(default=False)

    def as_json(self):
        return json.dumps(
            {
                'id': self.id,
                'title': self.title,
                'body': self.body,
                'author': self.author.email,
                'approved': self.approved
            }
        )

    def __str__(self):
        return self.title
