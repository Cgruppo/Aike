#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from app.friendApp.views import v_friend, v_friendadd

urlpatterns = patterns('',
    url(r'^$',v_friend),
    url(r'^add/u(\d+)/$',v_friendadd),
    )
