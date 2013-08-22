#-*- coding:utf-8 -*-
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render_to_response,RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic import ListView, CreateView, DeleteView, DetailView
from view.utils import myrender_to_response
from app.userApp.models import User
from django.contrib import messages
from app.activityApp.models import Activity,Comment
from app.userApp.models import AikeUser
from app.activityApp.forms import CommentAddForm,ActivityCreateForm
from app.qrcodeApp.utils import Qrcode,qr_get

# Create your views here.
@login_required
def v_create(request):
    """活动创建页"""
    data={}
    if request.method=="GET":
        acf = ActivityCreateForm()
        data['ActivityCreateForm'] = acf
        return myrender_to_response(request,'activity/create.tpl',data)
    elif request.method == "POST" :
        acf = ActivityCreateForm(request.POST)
        if acf.is_valid():
            ac = acf.save(commit=False)
            ac.creater = request.user
            ac.save()
            ac.organizer.add(request.user)
            ac.save()
            messages.success(request,"创建成功")
            print "success"
            return HttpResponseRedirect(reverse('activity_create'))
        else :
            print "faile"
            print acf.errors
            messages.error(request,"请检验数据是否符合格式")
            return HttpResponseRedirect(reverse('activity_create'))


class ActivityListView(ListView):
    #获得所有活动
    model = Activity
    context_object_name = "activitys"
    #paginate_by = 15
    #def get_context_data(self):
        #pass

# Old
def v_show(request):
    """活动展示页"""
    data={}
    #获得所有活动
    data['activitys']=Activity.objects.all()
    return myrender_to_response(request,'activity/show.tpl',data)

class ActivityDetailView(DetailView):
    model = Activity
    context_object_name = "activity"

    def get_context_data(self,**kwargs):
        context = super(ActivityDetailView,self).get_context_data(**kwargs)
        activity = context["activity"]
        try :
            if activity.activity_participant.get(user=request.user):
                hasjoin = True
            #except participantRelation.DoesNotExist:
        except :
            hasjoin = False
            context['hasjoin'] = hasjoin
            context['comments'] = activity.comment_activity.all()
            context['comment_add'] = CommentAddForm()
        return context


# Old
def v_acitem(request,acid):
    """活动展示单页"""
    data={}
    acid=int(acid)
    #试图用活动ID从数据库得到活动
    try :
        ac = Activity.objects.get(id=acid)
    except Activity.DoesNotExist:
        ac = None
    if request.method=='GET':
        if ac:
            data['title'] = ac.name
            data['activity'] = ac
            #判断用户是否已经参加
            try :
                if request.user == ac.participantR_activity.get(user=request.user).user:
                    hasjoin = True
            #except participantRelation.DoesNotExist:
            except :
                hasjoin = False
            data['hasjoin'] = hasjoin
            #获取该活动的所有评论
            data['comments'] = ac.comment_activity.all()
            ca = CommentAddForm()
            data['comment_add'] = ca
            return myrender_to_response(request,'activity/acitem.tpl',data)
        else :
            data['info'] = u'您要搜索的活动不存在！'
            return myrender_to_response(request,'info.tpl',data)
    else :
        if request.user.is_authenticated():
            ca = CommentAddForm(request.POST)
            if ca.is_valid():
                cd = ca.cleaned_data
                c = Comment.objects.create(owner=request.user,activity=ac,text=cd['text'])
            return HttpResponseRedirect('./')
        else :
            return HttpResponseRedirect('/login/')


@login_required
def v_acitemadmin(request,acid):
    '''活动信息管理'''
    data={}
    if request.user.is_authenticated():
        user = request.user
        try :
            #判断活动是否存在
            ac = Activity.objects.get(id=acid)
            try :
                #判断活动和用户是否是举办关系
                ac.organizer.get(username=user.username)
            except User.DoesNotExist:
                messages.warning(request,u"你没有对该活动修改的权限")
                return myrender_to_response(request,'info.tpl',data)

            if request.method == 'GET':
                data['activity'] = ac
                acf = ActivityCreateForm(initial={'name':ac.name,'introduction':ac.introduction,'date':ac.date,'place':ac.place,'price':ac.price,'category':ac.category})
                data['activityChangeForm'] = acf
                return myrender_to_response(request,'activity/acitemadmin.tpl',data)
            else :
                acf = ActivityCreateForm(request.POST)
                if acf.is_valid():
                    cd = acf.cleaned_data
                    ac.name=cd['name']
                    ac.introduction=cd['introduction']
                    ac.date=cd['date']
                    ac.place=cd['place']
                    ac.price=cd['price']
                    #ac.category = cd['category']
                    ac.save()
                    return HttpResponseRedirect('./')
                else :
                    data['info']=u"数据有误"
                    return myrender_to_response(request,'info.tpl',data)

        except Activity.DoesNotExist:
            ac = None
            data['info']=u"你要修改的活动不存在"
            return myrender_to_response(request,'info.tpl',data)        
    else :
        return HttpResponseRedirect('/login/')

@login_required
def v_addOrganizer(request,acid):
    '''添加举办者'''
    #TODO 添加活动举办者应只能从好友中添加,并自动提示
    data={}
    acid = int(acid)
    ac = Activity.objects.get(id=acid)
    aikeuser = AikeUser.objects.get(alias=request.GET['alias'])
    organizer = aikeuser.user
    ac.organizer.add(organizer)
    messages.success(request,u"已经添加了%s共同举办%s活动"%(aikeuser.alias,ac.name))
    return myrender_to_response(request,'info.tpl',data)

@login_required
def v_join(request,acid):
    """活动报名功能"""
    acid=int(acid)
    user = request.user
    ac = Activity.objects.get(id=acid)
    #获取所有已报名参加的人
    pt = ac.participant.filter(username=user.username)
    if pt :
        messages.info(request,u"你已经报名参加，请不要重复提交！")
    else:
        ac.participant.add(user)
        messages.success(request,u"你已经成功报名参加%s活动"%ac.name)
    return HttpResponseRedirect(reverse("activity_list"))

@login_required
def v_remove(request,acid):
    """活动退出功能"""
    acid=int(acid)
    user = request.user
    ac = Activity.objects.get(id=acid)
    ac.participant(request.user)
    messages.info(request,u"你已经退出%s活动"%ac.name)
    return HttpResponseRedirect(reverse("activity_list"))

@login_required
def v_qrcode(request,acid):
    """电子票管理界面"""
    data = {}
    try:
        ac = Activity.objects.get(id=acid)
    except Activity.DoesNotExist:
        ac = None
    if ac:
        data['activity']=ac
        try:
            pt = ac.participant.filter(username=request.user.username)
        except User.DoesNotExist:
            #TODO
            pt = None
            #生成电子票，第一个参数为内容，第二个参数为图片名字，第三个参数为宽
        if pt:
            q = Qrcode(acid,ac.id,100)
            data["has_per"] = True
        return myrender_to_response(request,'activity/qrcode.tpl',data)
    else:
        message.error(request,u"不存在该活动")
        return HttpResponseRedirect(reverse("activity_list"))

