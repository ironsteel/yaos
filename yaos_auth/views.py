from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from forms import RegisterForm
from django.contrib.auth import logout
from yaos_home.utils import *

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/");
    else:
        form = RegisterForm()
    return render_to_response("register.html", add_common_vars(request, {'form': form, 'logged_in': request.user.is_authenticated(), }), context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/")
