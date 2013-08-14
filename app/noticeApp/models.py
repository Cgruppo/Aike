#-*- coding:utf-8 -*-
from django.db import models
from app.userApp.models import User

# Create your models here.

class AddFriendNotice(models.Model):
	#添加好友消息通知
	owner = models.ForeignKey(User,related_name="addfriendnotice_owner")
	to = models.ForeignKey(User,related_name="addfriendnotice_to")
	date = models.DateField(auto_now_add=True)
	hasdone = models.BooleanField()
	def __unicode__(self):
		return u'%s添加%s' % (self.owner.alias,self.to.alias)
