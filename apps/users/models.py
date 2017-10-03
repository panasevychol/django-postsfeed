# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid

from django.db import models

from apps.users.constants import PASSWORD_MAX_LENGTH, ROLES

class User(models.Model):
    ROLE_CHOICES = ((value, key) for key, value in ROLES.items())

    email = models.EmailField()
    password = models.CharField(max_length=PASSWORD_MAX_LENGTH)
    role = models.SmallIntegerField(choices=ROLE_CHOICES,
                                    default=ROLES['reporter'])
    token = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )

    @property
    def profile(self):
        return {
            'email': self.email,
            'role': next(role for role, id in ROLES.items() if id == self.role)
        }

    def __str__(self):
        return self.email
