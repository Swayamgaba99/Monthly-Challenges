from django.urls import path

from . import views

urlpatterns = [
    path("<friend>",views.friend_char)
]