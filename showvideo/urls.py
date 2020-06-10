from django.urls import re_path
from . import views

# 456/
urlpatterns = [
    re_path("123/", views.hello),
    re_path("456/", views.world, name="main_page"),
    re_path("comment/(?P<id>\d+)/", views.accept_comment),
    re_path("one_video/(?P<id>\d+)/", views.one_video)
]