from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class LoginRequired(object):
  @method_decorator(login_required)
  def dispatch(self, request, *args, **kwargs):
      return super(LoginRequired, self).dispatch(request, *args, **kwargs)
