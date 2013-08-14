#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from app.apiApp.api import api_login,api_logout,api_getUser,api_getAc,api_getQr

urlpatterns = patterns('',
	url(r'^login/$',api_login),
	url(r'^logout/$',api_logout),
	#获取用户信息
	url(r'^getuser/',api_getUser),
	#获取活动信息
	url(r'^getac/$',api_getAc),
	url(r'^getqr/$',api_getQr),
)
