import json
from datetime import datetime

import numpy
from django.http import HttpResponse
from django.shortcuts import render

from apps.ves.models import *


def showTrailer(request):
    trailer = CatalogTrailer.objects.all()
    agent = Agent.objects.all()
    data = {'trailer':trailer,'agent':agent}
    return render(request, 'newData/catalog_trailer.html', data)


def AddTrailer(request):
    form = request.POST
    form = request.POST
    form._mutable = True
    if (not 'agent' in form):
        form['agent'] = None
    if (not 'model' in form):
        form['model'] = None
    if not form['tara'].isnumeric():
        form['tara'] = 0.0
    trailer = CatalogTrailer(number=form['number'], agent_id=form['agent'],model=form['model'],tara=form['tara'])
    trailer.save()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def UpdTrailer(request):
    form = request.POST
    form = request.POST
    form._mutable = True
    if (not 'agent' in form):
        form['agent'] = None
    if not form['tara'].isnumeric():
        form['tara'] = 0.0
    if (not 'model' in form):
        form['model'] = None
    trailer = CatalogTrailer.objects.filter(id=form['id'])
    trailer.update(number=form['number'], agent_id=form['agent'],model=form['model'],tara=form['tara'])
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')


def deleteTrailer(request):
    form = request.POST
    trailer = CatalogTrailer.objects.filter(id=form['id'])
    trailer.delete()
    payload = {'success': True}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')
