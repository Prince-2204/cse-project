# decorators.py

from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import Group
from django.shortcuts import render,HttpResponse,redirect

def faculty_required(view_func):
    def _wrapped_view(request, *args, **kwargs):
        if request.user.groups.filter(name='Faculty').exists():
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponse("You are not authenticated to access this page.", status=401)
    return _wrapped_view
