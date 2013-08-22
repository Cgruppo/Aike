#-*- coding:utf-8 -*-
from django.conf.urls import patterns, include, url
from view.view import v_index,v_help,v_test
from app.userApp.views import v_logout,v_register,v_visit
from app.activityApp.views import v_create
from app.qrcodeApp.utils import qr_per

#API接口
#from view.api import api_login
# Uncomment the next two lines to enable the admin:

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',v_index),
    url(r'^myspace/',include('app.userApp.urls')),
    url(r'^u(\d+)/$',v_visit),
    url(r'^show/',include('app.activityApp.urls')),
    url(r'^friend/',include('app.friendApp.urls')),
    url(r'^create/$',v_create,name="activity_create"),
    url(r'^login/$', 'django.contrib.auth.views.login', \
            {'template_name': 'login.tpl'}, name='logon'),
    url(r'^logout/$',v_logout),
    url(r'^help/$',v_help),
    url(r'^register/$',v_register,name="register"),
    #test
    url(r'^test/$',v_test),

    url(r'^static/qrcode',qr_per),
#    url(r'^rejson/$',rejson),
    # Examples:
    # url(r'^$', 'Aike.views.home', name='home'),
    # url(r'^Aike/', include('Aike.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

#API请求
urlpatterns += patterns('',
    #用于登陆
    url(r'^api/',include('app.apiApp.urls')),
    )
