#-*- coding:utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext

#自定义render_to_response，将request封装到response返回到模板

def myrender_to_response(request,template,data={}):
    if request.user.is_authenticated():
        #默认为模板添加消息通知信息
        #data['addfriendNs'] = request.user.addfriendnotice_to.filter(readed=False)
        pass
    return render_to_response(template,data,context_instance=RequestContext(request))

