from models import User

class UserAuth(object):
	def authenticate(self,account=None,password=None):
		try:
			user = User.objects.get(account=account)
		except User.DoesNotExist:
			pass
		else:
			if user.check_password(password):
				return user
		return None
	def get_user(self,user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None
