# -*- coding:utf-8 -*-
#This app use to create qrcode
#依赖PIL、qrencode、如果生成扩展名为png还需要libpng
from view.utils import myrender_to_response
from django.http import HttpResponse
from app.activityApp.models import Activity
import os
import Image
from qrencode import Encoder

class Qrcode:
    def    __init__(self,qname,qstr,width):
        self.qstr = u"%s" % qstr
        self.width = int(width)
        q = Encoder()
        isexist = os.path.isfile(u"./static/qrcode/%s.gif" % qname)
        if isexist:
            img = Image.open(u"./static/qrcode/%s.gif" % qname)
        else:
            img = q.encode(self.qstr,{"width":width})
            img.save(u"./static/qrcode/%s.gif" % qname)
    

def qr_per(request):
    user = request.user
    if user.is_authenticated():
        return
    else:
        data={}
        data["info"] = u"你没有权限"
        return myrender_to_response(request,"info",data)

def qr_get(request,acid):
    user = request.user
    data={}
    try:
        ac = Activity.objects.get(id=acid)
    except Activity.DoesNotExist:
        #TODO
        ac = None
    if ac:
        try:
            pt = ac.participant.filter(username=user.username)
        except UserDoseNotExist.DoesNotExist:
            #TODO
            pt = None
        if pt:
            img = open(u"./static/qrcode/%s.gif" % acid ,"rb").read()
            return HttpResponse(img,mimetype="image/gif")
        else:
            data["info"] = u"对不起，您未报名参加该活动，没有权限获取电子票!"
            return myrender_to_response(request,"info.tpl",data)
    else:
        data["info"] = u"对不起，该活动不存在!"
        return myrender_to_response(request,"info.tpl",data)