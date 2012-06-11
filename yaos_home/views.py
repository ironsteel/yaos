from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext


def home(request):
    return render_to_response("index.html", { 'is_logged': request.user.is_authenticated(), }, context_instance=RequestContext(request))

