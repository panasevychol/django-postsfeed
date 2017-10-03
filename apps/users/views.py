# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponseBadRequest, HttpResponse, JsonResponse
from django.shortcuts import render

from apps.users.constants import ROLES
from apps.users.models import User
from apps.users.utils import validate_user_email, validate_user_password


def register(request):
    email, password, role = [
        request.GET.get(key) for key in ('email', 'password', 'role')
    ]

    if not all([validate_user_email(email), validate_user_password(password)]):
        return HttpResponseBadRequest('Invalid email or password')

    if role not in ROLES.keys():
        return HttpResponseBadRequest(
            'Invalid role. Please choose one of theese: {}'
            .format(ROLES.keys())
        )
    User.objects.create(email=email, password=password, role=ROLES[role])
    return HttpResponse(
        'User successfully created. Email {}, role {}.'.format(email, role)
    )


def get_token(request):
    email, password = [request.GET.get(key) for key in ('email', 'password')]

    if not all([validate_user_email(email), validate_user_password(password)]):
        return HttpResponseBadRequest('Invalid email or password')

    user = User.objects.filter(email=email, password=password).first()
    if not user:
        return HttpResponseBadRequest('Wrong email of password')

    return HttpResponse(user.token)


def get_profile(request):
    token = request.GET.get('token')
    if not token:
        return HttpResponseBadRequest('Token required')

    user = User.objects.filter(token=token).first()
    if not user:
        return HttpResponseBadRequest('User not found')

    return JsonResponse(user.profile)
