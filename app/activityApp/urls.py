#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from app.activityApp.views import v_show, v_acitem, v_join, v_remove, v_qrcode,v_acitemadmin,v_addOrganizer
from app.qrcodeApp.utils import qr_get

urlpatterns = patterns('',
	url(r'^$',v_show),
	url(r'^ac(\d+)/$',v_acitem),
	url(r'^ac(\d+)/join/$',v_join),
	url(r'^ac(\d+)/remove/$',v_remove),
	url(r'^ac(\d+)/acitemadmin/$',v_acitemadmin),
	url(r'^ac(\d+)/qrcode/$',v_qrcode),
	url(r'^ac(\d+)/qrget/$',qr_get),
	url(r'^ac(\d+)/acitemadmin/addorganizer/$',v_addOrganizer),
)
