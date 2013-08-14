#-*- coding:utf-8 -*-
from django import forms

class UserRegisterForm(forms.Form):
	account = forms.CharField(label="帐号",help_text="用于登陆，长度为3-15")
	password = forms.CharField(widget=forms.PasswordInput,label="密码")
	alias = forms.CharField(required=False,label="别名",help_text="用于在网站中显示给其他人的名称")
	name = forms.CharField(required=False,label="真名")
	email = forms.EmailField(required=False,label="Email")
	sex = forms.ChoiceField(required=False,widget=forms.RadioSelect(),choices=((0,u'高富帅'),(1,u'白富美')),label="性别")
	age = forms.IntegerField(required=False,label="年龄")
	city = forms.CharField(required=False,label="所在城市",help_text="我们将优先通过地域给您展示活动")
	university = forms.CharField(required=False,label="大学",help_text="如果您是大学生，我们会优先将您所在大学的活动推荐给您")
	lbs = forms.CharField(required=False,label="上一次手机登陆地理位置")
	Auth = forms.BooleanField(required=False,label="认证")

class UserChangeForm(forms.Form):
#	account = forms.CharField(label="帐号")
#	password = forms.CharField(widget=forms.PasswordInput,label="密码")
	alias = forms.CharField(required=False,label="别名",help_text="用于在网站中显示给其他人的名称")
	name = forms.CharField(required=False,label="真名")
	email = forms.EmailField(required=False,label="Email")
	sex = forms.ChoiceField(widget=forms.RadioSelect(),choices=((0,u'高富帅'),(1,u'白富美')),label="性别")
	age = forms.IntegerField(required=False,label="年龄")
	city = forms.CharField(required=False,label="所在城市",help_text="我们将优先通过地域给您展示活动")
	university = forms.CharField(required=False,label="大学",help_text="如果您是大学生，我们会优先将您所在大学的活动推荐给您")
	lbs = forms.CharField(required=False,label="上一次手机登陆地理位置")
	Auth = forms.BooleanField(required=False,label="认证")
	
class UserMessageBoardForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea(attrs={'class':'span5','rows':'5','style':'resize:none'}))
