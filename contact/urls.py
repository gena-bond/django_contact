from django.urls import path, re_path

from .views import *


urlpatterns = [
    path("", ContactViews.as_view(), name='home'),
    path("update/<int:pk>/", updatecontact, name='updatecontact'),
    path("addcontact/", addcontact, name='addcontact'),
]