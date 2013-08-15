#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from app.userApp.views import v_myspace,v_myinfo,v_mycreate,v_myjoin,v_mycomment,v_mymessage,v_mymessageboard

urlpatterns = patterns('',
    url(r'^$',v_myspace),
    url(r'^myinfo/$',v_myinfo),
    url(r'^mycreate/$',v_mycreate),
    url(r'^myjoin/$',v_myjoin),
    url(r'^mycomment/$',v_mycomment),
    url(r'^mymessage/$',v_mymessage),
    url(r'^mymessageboard/$',v_mymessageboard),
)
