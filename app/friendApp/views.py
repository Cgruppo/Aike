#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from view.utils import myrender_to_response
from app.userApp.models import User,Group
from app.noticeApp.models import AddFriendNotice

# Create your views here.
def v_friend(request):
	"""好友页面"""
	data={}
	data['nav3']=u"active"
	data['title']=u"好友"
	#如果未验证，跳转到登陆页
	if not request.user.is_authenticated():
		return HttpResponseRedirect('/login')
	if request.method=="GET":
		user = request.user
		groups = user.group_owner.all()
		data['groups']=groups
	#	data['friends'] = friends[0].member.all()[0].account
		return myrender_to_response(request,'friend.tpl',data)
	else :
		user = request.user
		friend = User.objects.get(alias=request.POST['alias'])
		groupname=request.POST['group']
		#向请求的好友中添加一条通知
		parameter=user.alias + ',' + groupname
		event = user.alias + u"请求添加你为好友"
		UserNotice.objects.create(owner=friend,noticecode=00,event=event,hasdone=False,parameter=parameter)
		return HttpResponseRedirect("./")

def v_friendadd(request,friendid):
	'''好友添加函数'''
	user = request.user
	data={}
	friend = User.objects.get(id=int(friendid))
	try:
		afn = AddFriendNotice.objects.get(to=user,owner=friend)
	except AddFriendNotice.DoesNotExist:
		afn = AddFriendNotice.objects.create(owner=user,to=friend,hasdone=False)
		data['info']=u"已经发送添加好友请求"
		return myrender_to_response(request,'info.tpl',data)
	afn.hasdone = True
	afn.save()
	#将好友添加到自己的未分组好友分组
	ug = user.group_owner.get(name=u"未分组")
	ug.member.add(friend)
	ug.save()
	#将自己添加到好友的未分组好友分组
	fg = friend.group_owner.get(name="未分组")
	fg.member.add(friend)
	fg.save()
	data['info'] = u"您已与%s成为了好友" % friend.alias
	return myrender_to_response(request,'info.tpl',data)
