# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import (
    JsonResponse, HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
)

from apps.posts.models import Post
from apps.posts.constants import (
    DEFAULT_LIMIT, DEFAULT_OFFSET, TITLE_MAX_LENGTH, BODY_MAX_LENGTH
)
from apps.posts.utils import check_role
from apps.users.models import User
from apps.users.constants import ROLES


def show(request):
    if (check_role(request, ROLES['editor'])
        or check_role(request, ROLES['reporter'])):

        posts_objs = Post.objects.all()

    else:
        posts_objs = Post.objects.filter(approved=True)


    title_contains = request.GET.get('title_contains')
    if title_contains:
        posts_objs = posts_objs.filter(title__icontains=title_contains)

    body_contains = request.GET.get('body_contains')
    if body_contains:
        posts_objs = posts_objs.filter(body__icontains=body_contains)

    limit = request.GET.get('limit', default=DEFAULT_LIMIT)
    offset = request.GET.get('offset', default=DEFAULT_OFFSET)

    posts = [post.as_json() for post in posts_objs[offset:offset+limit]]
    return JsonResponse(posts, safe=False)


def create(request):
    title, body, token = [
        request.GET.get(key) for key in ('title', 'body', 'token')
    ]
    if not title or len(title) > TITLE_MAX_LENGTH:
        return HttpResponseBadRequest('Invalid title')

    if not body or len(body) > BODY_MAX_LENGTH:
        return HttpResponseBadRequest('Invalid body')

    if not token:
        return HttpResponseBadRequest('Token is required')

    user = User.objects.filter(token=token).first()
    if not user:
        return HttpResponseBadRequest('Invalid token')

    if user.role not in (ROLES['editor'], ROLES['reporter']):
        return HttpResponseForbidden()

    Post.objects.create(title=title, body=body, author=user)
    return HttpResponse(
        'Post "{}" successfully created by {}.'.format(title, user.email)
    )


def approve(request):
    if not check_role(request, ROLES['editor']):
        return HttpResponseForbidden()

    id = request.GET.get('id', default=None)
    if not id:
        return HttpResponseBadRequest('post_id parameter is required')

    posts_obj = Post.objects.filter(id=id)
    if not posts_obj:
        return HttpResponseBadRequest('Post not found')

    posts_obj.update(approved=True)
    return HttpResponse('Post #{} successfully approved'.format(id))
