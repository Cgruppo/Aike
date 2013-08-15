#-*- coding:utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#以下为与活动相关的数据模型

class Comment(models.Model):
    #活动中用户的评论模型
    text = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    activity = models.ForeignKey('Activity',related_name='comment_activity')
    owner = models.ForeignKey(User,related_name='comment_owner')
    at = models.ManyToManyField(User,related_name='comment_at')
    def __unicode__(self):
        return u'%s:%s,Time:%s' % (self.owner.alias,self.text,self.date)

class Activity(models.Model):
    #活动模型
    name = models.CharField(max_length=30)
    introduction = models.TextField()
    date = models.DateField() #活动举办时间，应为DateTime类型，待改
    createdate = models.DateField(auto_now_add=True)
    place = models.CharField(max_length=30)
    price = models.IntegerField()
    category = models.CharField(max_length=30,null=True,blank=True,verbose_name="分类")
    creater = models.ForeignKey(User,related_name='activity_create')
    organizer = models.ManyToManyField(User,related_name="activity_organizer")
    sponsor = models.ManyToManyField(User,related_name="activity_sponsor")
    participant = models.ManyToManyField(User,related_name="activity_participant")
    
    def __unicode__(self):
        return u"%s" % self.name

class Team(models.Model):
    #活动举办者所在小组模型
    name = models.CharField(max_length=30)
    describe = models.TextField()
    date = models.DateField(auto_now_add=True) #用以记录小组创办时间
    member = models.ManyToManyField(User,related_name="team_member")
    activity = models.ManyToManyField(Activity,related_name="team_ctivity")
    def __unicode__(self):
        return self.name

class ActivityNotice(models.Model):
    #活动消息模型，用于通知活动举办者
    #参数列表暂定 0x用户相关信息，1x活动相关信息
    owner = models.ForeignKey(Activity,related_name="activitynotice_owner")
    event = models.CharField(max_length=30)
    readed = models.BooleanField(default=False)

    def __unicode__(self):
        return self.event

