from allauth.account.adapter import DefaultAccountAdapter, resolve_url, warnings
from allauth.utils import get_user_model
import settings

class ModelCarAccountAdapter(DefaultAccountAdapter):

    def get_login_redirect_url(self, request):
        url = getattr(settings, "LOGIN_REDIRECT_URLNAME", None)
        if url:
            warnings.warn("LOGIN_REDIRECT_URLNAME is deprecated, simply"
                          " use LOGIN_REDIRECT_URL with a URL name",
                          DeprecationWarning)
        else:
            url = settings.LOGIN_REDIRECT_URL
        return resolve_url(url)

    def new_user(self, request):
        print 'new user'
        if not request.user.is_anonymous():
            user = request.user
        else:
            user = get_user_model()()

        return user

    def populate_username(self, request, user):
        #data = form.cleaned_data
        #user.real_name = data.get("real_name")
        #user.is_agreed = data.get("is_agreed")
        #import pdb;pdb.set_trace()
        print 'populate user'
        print self
        print user
        return super(ModelCarAccountAdapter, self).populate_username(request, user)
