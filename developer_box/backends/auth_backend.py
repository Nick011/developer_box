from django.contrib.auth.models import User, check_password
from django.db.models import Q


class UsernameEmailBackend(object):
	def authenticate(self, username=None, password=None):
		users = User.objects.filter(Q(username__iexact=username) | Q(email__iexact=username))
		#is_valid = check_password(password, user.password)

		if len(users) and check_password(password, users[0].password):
			return users[0]

		return None

	def get_user(self, user_id):
		try:
			return User.objects.get(pk=user_id)
		except User.DoesNotExist:
			return None