class appdb(object):
    """A router to control all database operations on models in
    the myapp application"""

    def db_for_read(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        #if model._meta.app_label in ('userApp','activityApp'):
         #   return ('userdb','activitydb')
        #else :
        return self.__app_router(model)

    def db_for_write(self, model, **hints):
        "Point all operations on myapp models to 'other'"
        return self.__app_router(model)

    def allow_relation(self, obj1, obj2, **hints):
        "Allow any relation if a model in myapp is involved"
        if obj1._meta.app_label == obj2._meta.app_label :
            return True
        elif (obj1._meta.app_label in ('userApp','activityApp','noticeApp')) and (obj2._meta.app_label in ('userApp','activityApp','noticeApp')):
            return True

    def allow_syncdb(self, db, model):
        #print "model._meta.app_label = %s, db = %s", (model._meta.app_label, db)
        
        "Make sure the myapp app only appears on the 'other' db"
        return self.__app_router(model) == db
   
    def __app_router(self, model):
        if model._meta.app_label == 'userApp':
            return 'userdb'
        elif model._meta.app_label == 'activityApp':
            return 'activitydb'
        elif model._meta.app_label == 'messageApp':
            return 'messagedb'
	elif model._meta.app_label == 'noticeApp':
            return 'noticedb'
        else :
            return 'default'
            
