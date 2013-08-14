#-*- coding:utf-8 -*-
from django.http import HttpResponse
from django.contrib.auth import login,logout,authenticate
from app.userApp.models import User
from app.activityApp.models import Activity
import json

#测试函数在apiTest目录下,请求url请查看urls.py，返回格式参照浏览器返回样式解析

#登陆状态改为使用状态码
#0为未登录
#1为登陆成功
#2为已登陆
#3为cookies有效期已过

#5为用户名不存在
#6为密码错误
#7未使用POST登陆

#10为注销成功

def api_login(request):
	#仅供调试，在项目根目录生成
	#f = open('log.txt','w')
	#f.write(str(request))
	data={}
	if request.method=='POST':
		account = request.POST['account']
		password = request.POST['password']
		user = authenticate(account=account,password=password)
		if user is not None:
			login(request,user)
			data["code"]=1	
		else :
			try :
				if User.objects.get(account=account) is not None:
					data["code"]=6
			except User.DoesNotExist:
				data["code"]=5
	else :
		#暂定使用get请求时返回错误
		data["code"]=7
	return HttpResponse(json.dumps(data))

def api_logout(request):
	data={}
	logout(request)
	data["code"]="10"
	return json.dumps(data)

#TODO未完成测试
def api_getUser(request):
	data = {}
	user = request.user
	if user.is_authenticated():
		#获取指定用户的信息，看客户端传上来的请求
		#可以用json或者get指明要查询的人，这里目前是返回请求者的个人信息
		user = request.user
		data['code'] = 2
		userinfo = {}
		userinfo['account'] = user.account
		userinfo['alias'] = user.alias
		userinfo['name'] = user.name
		userinfo['email'] = user.email
#		性别为boolean类型，0为男，1为女
		userinfo['sex'] = user.sex
		userinfo['age'] = user.age
		userinfo['city'] = user.city
		userinfo['university'] = user.university
#		上一次登陆地理位置，待决定
#		userinfo['lbs'] = user.lbs
#		是否为认证用户，boolean类型，0为未认证
		userinfo['auth'] = user.auth
		userinfo['registerdate'] = u"%s" % user.registerdate
		data['userinfo'] = userinfo
	else :
		data['code'] = 0
	return HttpResponse(json.dumps(data))

#未完成测试
def api_getAc(request):
	#获取活动列表不要求先登陆
	data = {}
	#返回最新创建的20个活动
	activitysInfo = []
	activitys = Activity.objects.order_by("date")[0:20]
	for activity in activitys:
		activityInfo = {}
		activityInfo['name'] = activity.name
		#活动介绍目前暂时不包含图片，如果包含一些富媒体，再考虑解决方案
		activityInfo['introduction'] = activity.introduction
		activityInfo['place'] = activity.place
		activityInfo['price'] = activity.price
		activityInfo['category'] = activity.category
		#创建者
		activityInfo['creater'] = activity.creater.alias
		#组织者有多个，存在子列表
		organizerInfo = []
		for organizerR in activity.organizerR_activity.all():
			organizerInfo.append(organizerR.user.alias)
		activityInfo['organizer'] = organizerInfo
		#赞助商有多个，存在子列表
		sponsorInfo = []
		for sponsorR in activity.sponsorR_activity.all():
			sponsorInfo.append(sponsor.user.alias)
		activityInfo['sponsor'] = sponsorInfo
		activitysInfo.append(activityInfo)
	data['activity'] = activitysInfo
	return HttpResponse(json.dumps(data))

#初步测试通过
def api_getQr(request):
	acid=2
	img = open(u"./Aike/static/qrcode/%s.gif" % acid ,"rb")
	#接收时以bytes接收
	return HttpResponse(img)
