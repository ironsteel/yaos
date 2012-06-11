from django.conf.urls.defaults import *
from views import *
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
        url(r'register/$', register, name="register"),
        url(r'login/$', login, name="login"),
        url(r'logout/$', logout, name="logout"),

)
