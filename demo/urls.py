# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name='demo'
urlpatterns = [
    url(r'^category/$',views.category_table,name='category_table'),
    url(r'^category/(?P<index>.+)/$',views.category_detail,name='category'),
    url(r'^brand/$',views.brand_table,name='brand_table'),
    url(r'^brand/(?P<index>.+)/$',views.brand_detail,name='brand'),
    url(r'^model/$',views.model_table,name='model_table'),
    url(r'^model/(?P<index>.+)/$',views.model_detail,name='model'),
    ]
