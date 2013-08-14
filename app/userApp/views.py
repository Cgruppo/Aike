#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth import authenticate,login,logout
from view.utils import myrender_to_response
from app.userApp.models import User,Group,MessageBoard
from app.userApp.forms import UserRegisterForm,UserChangeForm,UserMessageBoardForm
from app.noticeApp.models import AddFriendNotice
# Create your views here.
#视图函数

def v_login(request):
	"""登陆界面"""
	data={}
	request.session['rurl'] = request.META.get('HTTP_REFERER','/myspace/')
	if request.method=="GET":
		return myrender_to_response(request,'login.tpl',data)
	else :
		account=request.POST['account']
		password=request.POST['password']
		#调用Auth框架验证函数，成功即返回用户，失败返回None
		user = authenticate(account=account,password=password)
		if user is not None:
			#Auth框架登陆函数
			login(request,user)
			return HttpResponseRedirect(request.session['rurl'])
		else:
			data['isLogin']	=u"请确认你的密码是否输入正确"
			return myrender_to_response(request,'login.tpl',data)

def v_logout(request):
	"""注销函数"""
	logout(request)
	return HttpResponseRedirect('/')

def v_register(request):
	"""注册页"""
	data={}
	#性别默认勾选为男
	form = UserRegisterForm(initial={'sex':0,})
	data['form']=form
	if request.method=='GET':
		return myrender_to_response(request,'register.tpl',data)
	else:
		uf = UserRegisterForm(request.POST)
		if uf.is_valid():
			cd = uf.cleaned_data
			user = User()
			user.account=cd['account']
			user.password=user.hashed_password(cd['password'])
			user.alias=cd['alias']
			user.name=cd['name']
			user.sex=bool(int(cd['sex']))
			user.email=cd['email']
			if cd['age']==None:
				user.age=0
			else:
				user.age=cd['age']
			user.city=cd['city']
			user.university=cd['university']
			user.lbs=''
			user.auth=False
			user.save()
			g1 = Group.objects.create(name=u"未分组",owner=user)
			g1.save()
			data['info']=u"注册成功！"
			return myrender_to_response(request,'info.tpl',data)
		else :
			data['form'] = uf
			error = {}
			span = {}
			for (errork,errorv) in uf.errors.iteritems():
				error[errork] = 'error'
				span[errork] = errorv
			data['error'] = error
			data['span'] = span
			return myrender_to_response(request,'register.tpl',data)
	#错误信息处理，待添加		
	#	else :
	#		data['info']=uf.errors

def v_myspace(request):
	"""个人的空间首页"""
	if request.user.is_authenticated():
		data={}
		data['nav1']=u"active"
		data['title']=u"个人空间"
		return myrender_to_response(request,'myspace.tpl',data)
	else:
		return HttpResponseRedirect('/login/')

def v_myinfo(request):
	"""个人信息页"""
	data={}
	if 	request.method=="GET":
		data['title']=u"我的个人信息"
		data['nav1']=u'active'
		user = request.user
		#新建个人信息页表单并初始化为当前用户信息
		ucf = UserChangeForm(initial={'alias':user.alias,'sex':int(user.sex),'name':user.name,'age':user.age,'city':user.city,'email':user.email,'university':user.university,'lbs':user.lbs,'auth':user.auth,})
		data['form']=ucf
		data['mypage']='myinfo.tpl'
		return myrender_to_response(request,'myspace.tpl',data)
	else:
		user = request.user
		ucf = UserChangeForm(request.POST)
		#如果数据是合法的同步数据到数据库
		if ucf.is_valid():
			cd = ucf.cleaned_data
			user.alias=cd['alias']
			user.name=cd['name']
			user.sex=bool(int(cd['sex']))
			user.email=cd['email']
			user.age=cd['age']
			user.city=cd['city']
			user.university=cd['university']
			user.save()
			#u.set_user(name=name,email=email,sex=sex,age=age,city=city,university=university)
			return HttpResponseRedirect("./")
		else:
			data['info']=u"请检测输入的数据是否有误！"
			return myrender_to_response(request,'info.tpl',data)

def v_mycreate(request):
	"""个人创建的活动管理页"""
	data={}
	data['nav1']=u"active"
	data['title']=u"我的创建的活动"
	#获取该用户举办的所有活动
	data['activitys']=request.user.organizerR_user.all()
	data['mypage'] = 'mycreate.tpl'
	return myrender_to_response(request,'myspace.tpl',data)

def v_myjoin(request):
	"""个人参与的活动管理页"""
	data={}
	data['nav1']=u"active"
	data['title']=u"我的参加的活动"
	#获取该用户参加的所有活动
	data['activitys']=request.user.participantR_user.all()
	data['mypage'] = 'myjoin.tpl'
	return myrender_to_response(request,'myspace.tpl',data)

def v_mycomment(request):
	"""在活动页面的评论"""
	data={}
	data['nav1']=u"active"
	data['title']=u"我的评论"
	data['comments'] = request.user.comment_owner.using('activitydb').all()
	data['mypage'] = 'mycomment.tpl'
	return myrender_to_response(request,'myspace.tpl',data)

def v_mymessage(request):
	"""站内信管理页"""
	data={}
	data['nav1']=u"activie"
	data['title']=u"站内信"
	data['mymessages'] = request.user.message_owner.all()
	data['tomessages'] = request.user.message_to.all()
	data['mypage'] = 'mymessage.tpl'
	return myrender_to_response(request,'myspace.tpl',data)

def v_mymessageboard(request):
	"""留言板管理页面"""
	data={}
	data['nav1'] = u"active"
	data['title'] = u"留言板"
	if request.method == "GET":
		umbf = UserMessageBoardForm()
	else :
		umbf = UserMessageBoardForm(request.POST)
		if umbf.is_valid():
			cd = umbf.cleaned_data
			mb = MessageBoard.objects.create(owner=request.user,to=visitor,text=cd['text'])
			return HttpResponseRedirect('./')
	data['form'] = umbf
	messageboards = request.user.messageboard_to.all()
	data['messageboards'] = messageboards
	data['mypage'] = 'mymessageboard.tpl'
	return myrender_to_response(request,'myspace.tpl',data)

def v_visit(request,uid):
	#被访问者
	uid = int(uid)
	try:
		visitor = User.objects.get(id=uid)
	except User.DoesNotExist:
		visitor = None
	data = {}
	if visitor:
		if request.method=='GET':
			data['visitor'] = visitor
			#显示5个最近组织的活动
			organizerRs = visitor.organizerR_user.all().order_by('date')[0:5]
			data['organizerRs'] = organizerRs
			participantRs = visitor.participantR_user.all().order_by('date')[0:5]
			data['participantRs'] = participantRs

			#空白留言板
			umbf = UserMessageBoardForm()
			data['form'] = umbf

			messageboards = visitor.messageboard_to.all()
			data['messageboards'] = messageboards
			return myrender_to_response(request,'visit.tpl',data)
		else :
			#获取提交的留言板内容
			umbf = UserMessageBoardForm(request.POST)
			if umbf.is_valid():
				cd = umbf.cleaned_data
				mb = MessageBoard.objects.create(owner=request.user,to=visitor,text=cd['text'])
				return HttpResponseRedirect('./')
	else :
		data['info'] = u'抱歉，您要查询的用户不存在！'
		return myrender_to_response(request,'info.tpl',data)
