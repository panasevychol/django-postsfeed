from django.conf.urls import url

from apps.posts.views import show, approve, create

urlpatterns = [
    url(r'^show', show),
    url(r'^create/', create),
    url(r'^approve/', approve),
]
