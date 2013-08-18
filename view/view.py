#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth import authenticate,login,logout
from utils import myrender_to_response#再次封装，返回带request到模板
from app.userApp.models import User,Group
from app.activityApp.models import Activity
from app.userApp.forms import UserRegisterForm,UserChangeForm
from app.activityApp.forms import CommentAddForm,ActivityCreateForm
import json
import datetime
import Image

#主要是login_view这个函数还有问题
#视图函数

#测试二维码访问权限
def v_test(request):
    img = Image.open(u"./Aike/static/qrcode/2.gif")
    data={}
    data["img"] = img
    return render_to_response('test.tpl',data)

def v_index(request):
    """用于展示首页"""
    data={}
    if request.user.is_authenticated():
        data['user']=request.user.account
    data['title']="爱克,释放你的活力！"
    data['activitycount'] = len(Activity.objects.all())
    data['usercount'] = len(User.objects.all())
#    return render_to_response('index.tpl',data,context_instance=RequestContext(request))
    return myrender_to_response(request,'index.tpl',data)


#TODO 活动分类

def v_help(request):
    """帮助页"""
    return myrender_to_response(request,'help.tpl',{})

#仅测试使用
def rejson(request):
    d = {'key1':'测试','key2':['1','2']}
    j = json.dumps(d)
    return HttpResponse(j)

