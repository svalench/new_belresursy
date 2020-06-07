import json
from datetime import datetime
from django.contrib.auth.models import User
import numpy
from django.http import HttpResponse
from django.shortcuts import render

from apps.ves.models import *


def AddUserNew(request):
    form = request.POST
    user = User(name=form['nikname'], first_name=form['ferst_name'], secondName=form['second_name'], lastName = form['last_name'],
                         role=form['role'],user_role=form['access'])
    user.set_password(form['pass'])
    user.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def UpdUser(request):
    form = request.POST
    user = User.objects.filter(id=form['id'])
    user.update(name=form['nikname'], first_name=form['ferst_name'], secondName=form['second_name'], lastName = form['last_name'],
                         role=form['role'],user_role=form['access'])
    u = User.objects.get(id=form['id'])
    u.set_password(form['pass'])
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def deleteUser(request):
    form = request.POST
    trailer = User.objects.filter(id=form['id'])
    trailer.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')
