#-*- coding:utf-8 -*-
from django.db import models
from app.userApp.models import User

# Create your models here.
#以下为与活动相关的数据模型

class Comment(models.Model):
	#活动中用户的评论模型
	text = models.CharField(max_length=200)
	date = models.DateTimeField(auto_now_add=True)
	activity = models.ForeignKey('Activity',related_name='comment_activity')
	owner = models.ForeignKey(User,related_name='comment_owner')
	at = models.ManyToManyField(User,related_name='comment_at',through='atRelation')
	def __unicode__(self):
		return u'%s:%s,Time:%s' % (self.owner.alias,self.text,self.date)

#Comment中at的多对多映射
class atRelation(models.Model):
	comment = models.ForeignKey(Comment,related_name="atR_comment")
	owner = models.ForeignKey(User,related_name="atR_owner")
#--------------------------

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
	organizer = models.ManyToManyField(User,related_name="activity_organizer",through="organizerRelation")
	sponsor = models.ManyToManyField(User,related_name="activity_sponsor",through='sponsorRelation')
	participant = models.ManyToManyField(User,related_name="activity_participant",through='participantRelation')
	
	def __unicode__(self):
		return u"%s" % self.name

#Activity的多对多映射
class organizerRelation(models.Model):
	activity = models.ForeignKey(Activity,related_name="organizerR_activity")
	user = models.ForeignKey(User,related_name="organizerR_user")
	date = models.DateField(auto_now_add=True) #用户参与的时间，以下类似

class sponsorRelation(models.Model):
	activity = models.ForeignKey(Activity,related_name="sponsorR_activity")
	user = models.ForeignKey(User,related_name="sponsorR_user")
	date = models.DateField(auto_now_add=True)

class participantRelation(models.Model):
	activity = models.ForeignKey(Activity,related_name="participantR_activity")
	user = models.ForeignKey(User,related_name="participantR_user")
	date = models.DateField(auto_now_add=True)
#---------------------


class Team(models.Model):
	#活动举办者所在小组模型
	name = models.CharField(max_length=30)
	describe = models.TextField()
	date = models.DateField(auto_now_add=True) #用以记录小组创办时间
	member = models.ManyToManyField(User,related_name="team_member",through="memberRelation")
	activity = models.ManyToManyField(Activity,related_name="teama_ctivity",through="activityRelation")
	def __unicode__(self):
		return self.name

#Team中的多对多映射
class memberRelation(models.Model):
	user = models.ForeignKey(User,related_name="memberR_user")
	team = models.ForeignKey(Team,related_name="memberR_team")
	date = models.DateField(auto_now_add=True) #用以记录加入用户小组的时间

class activityRelation(models.Model):
	team = models.ForeignKey(Team,related_name="activityR_team")
	activity = models.ForeignKey(Activity,related_name="activityR_activity")
#--------------------

class ActivityNotice(models.Model):
	#活动消息模型，用于通知活动举办者
	#参数列表暂定 0x用户相关信息，1x活动相关信息
	owner = models.ForeignKey(Activity,related_name="activitynotice_owner")
	event = models.CharField(max_length=30)
	noticecode = models.IntegerField()
	hasdone = models.BooleanField()
	parameter = models.CharField(max_length=30)
