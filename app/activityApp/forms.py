#-*- coding:utf-8 -*-
from django import forms
	
class ActivityCreateForm(forms.Form):
	name = forms.CharField(label="活动名称")
	introduction = forms.CharField(label="简介",widget=forms.Textarea(attrs={'class':'span6','row':'5','style':'resize:none'}))
	place = forms.CharField(label="地点")
	price = forms.IntegerField(label="价格")
	date = forms.DateField(label="举办时间",widget=forms.DateInput(attrs={'placeholder':'格式举例:2013-01-17'}))


class CommentAddForm(forms.Form):
	text = forms.CharField(widget=forms.Textarea(attrs={'class':'span6','rows':'5','style':'resize:none',}))
