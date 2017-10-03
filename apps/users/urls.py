from django.conf.urls import url

from apps.users.views import register, get_token, get_profile

urlpatterns = [
    url(r'^register/', register),
    url(r'^get-token/', get_token),
    url(r'^get-profile/', get_profile),
]
