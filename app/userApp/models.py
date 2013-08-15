#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import hashlib
# Create your models here.

class AikeUser(models.Model):
    #用户数据模型
    user = models.ForeignKey(User)
    alias = models.CharField(max_length=30,verbose_name="别名")
    name = models.CharField(max_length=30,null=True,verbose_name="真名")
    email = models.EmailField(null=True,verbose_name="邮箱")
    sex = models.BooleanField(verbose_name="性别")
    age = models.IntegerField(verbose_name="年龄")
#    preference = models.CharField()
    city = models.CharField(max_length=30,null=True,verbose_name="所在城市")
    university = models.CharField(max_length=30,null=True,verbose_name="就读大学")
    lbs = models.CharField(max_length=30,null=True,verbose_name="上一次登陆地理位置")
    auth = models.BooleanField(verbose_name="认证")
    registerdate = models.DateField(auto_now_add=True,editable=False,verbose_name="注册日期")
#    friend = models.ManyToManyField("self")

    def __unicode__(self):
        return self.user.username

class Group(models.Model):
    #用户好友分组模型
    name = models.CharField(max_length=30)
    member = models.ManyToManyField(User,related_name="group_member")
    owner = models.ForeignKey(User,related_name="group_owner")
    def __unicode__(self):
        return u'%s的好友分组：%s' % (self.owner.alias,self.name)

class Message(models.Model):
    #用户站内信模型
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,related_name='message_owner')
    to = models.ForeignKey(User,related_name='message_to')
    def __unicode__(self):
        return u'%s回复%s:%s' % (self.owner.alias,self.to.alias,self.text)

class MessageBoard(models.Model):
    #留言板模型
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User,related_name='messageboard_owner')
    to = models.ForeignKey(User,related_name="messageboard_to")
    def __unicode__(self):
        return u'%s回复%s:%s' % (self.owner.alias,self.to.alias,self.text)
