# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='demo'
urlpatterns = [
    url(r'^(?P<index>.+)', views.model_detail, name='model')
    ]
