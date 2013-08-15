from django.contrib import admin
from app.activityApp.models import Comment, Activity, Team, ActivityNotice
from app.userApp.models import AikeUser, Group, Message, MessageBoard
#from app.friendApp.models import *
#from app.noticeApp.models import *

admin.site.register(Comment)
admin.site.register(Activity)
admin.site.register(Team)
admin.site.register(ActivityNotice)

admin.site.register(AikeUser)
admin.site.register(Group)
admin.site.register(Message)
admin.site.register(MessageBoard)
