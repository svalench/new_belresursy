"""ves_n URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from apps.ves.add_in_db import addAutoNew, addVagonNew,updateAutoNew, updateTrainNew , updateDDAutoNew
from apps.ves.contract import showContract, AddContract, UpdContract, deleteContract
from apps.ves.detectNumber import detectNumber
from apps.ves.production import showProduction, AddProduction, UpdProduction, deleteProduction
from apps.ves.responseblePerson import showPerson, AddPerson, UpdPerson, deletePerson
from apps.ves.trailer import showTrailer, UpdTrailer, AddTrailer, deleteTrailer
from apps.ves.addUser import  UpdUser, AddUserNew, deleteUser
from apps.ves.docGeneration import actGenerate, nakladnaia_book,nakladnaia_vertical,actGenerateZD
from ves_n.views import *
from apps.ves.plc_svet import *
from channels.routing import ProtocolTypeRouter
from django.views.defaults import server_error, page_not_found, permission_denied
application = ProtocolTypeRouter({
    # Empty for now (http->django views is added by default)
})

urlpatterns = [
    path('', include('apps.ves.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('logout', logout_view, name = 'logout'),
    path('addaction/',addactionView, name='addaction'),

    path('addvagonPOST/',addVagonPost, name='addVagonPOST'),
    path('addcontragentPOST/', addContragentView, name='addcontragentPOST'),
    path('updcontragentPOST/', updContragentView, name='updcontragentPOST'),
    path('delete/agent/all', deleteContragentView, name='deleteContragentView'),
    path('getDataAuto/', GetDataAuto, name='getDataAuto'),
    path('getDataZd/', GetDataZd, name='getDataZd'),
    path('getDataStatus/', GetDataStatus, name='getDataStatus'),
    path('getDataZd/getzdnumbler', GetZdNumber, name='getZdNumber'),
    path('getDataZd/getzdagent', GetZdAgent, name='getZdAgent'),
    path('getDataZd/getzddate', GetZdDate, name='getZdDate'),

    path('getDataAuto/getautonumbler', GetAutoNumber, name='getAutoNumber'),
    path('getDataAuto/getautoagent', GetAutoAgent, name='getAutoAgent'),
    path('getDataAuto/getautodate', GetAutoDate, name='getAutoDate'),

    path('onoff/svet1/',onOffS1,name='on1'),
    path('onoff/vezd/',svetoforFromStreetOnScale,name='sulnaves'),
    path('onoff/viezd/', svetoforFromScaleOnTerritory, name='svesonter'),
    path('onoff/fromul/',svetoforFromTerritoryOnScale, name='steronscale'),
    path('onoff/toul/', svetoforFromScaleOnStreet, name='fromscaletoul'),
    path('onoff/zd/svet1/',onOffZd,name='onoffzd'),
    path('add/auto/new',addAutoNew,name='newAddAuto'),
    path('upd/auto/data/new',updateAutoNew,name='updNewAuto'),
    path('add/train/new',addVagonNew,name='newAddVagon'),
    path('upd/train/data/new', updateTrainNew, name='updNewTrain'),
    path('detect/auto/number', detectNumber, name='detectNumber'),

#обновления данных из подробнее
    path('upd/data/moreinfo',updateDDAutoNew,name='updInfoMore'),

# xls накладная горизонтальная
    path('download/xls/gorizontal/',nakladnaia_book,name='xlsGenerateGorizontaly'),
    path('download/xls/vert/',nakladnaia_vertical,name='xlsGenerateVert'),

    #данные бд контрагент
    path('data/catalogContract',showContract,name='catalogcontract'),
    path('data/catalogContractAdd',AddContract,name='catalogcontractAdd'),
    path('data/catalogContractUpd',UpdContract,name='catalogcontractUpd'),
    path('data/catalogContractDel', deleteContract, name='catalogcontractDel'),

    # users
    path('data/add/user/new',AddUserNew,name='addUser'),
    path('data/update/user/new',UpdUser,name='updUser'),
    path('data/delete/user/',deleteUser,name='deleteUser'),
    # прицепы
    path('data/trailerShow',showTrailer,name='trailerShow'),
    path('data/trailerAdd',AddTrailer,name='trailerAdd'),
    path('data/trailerUpd',UpdTrailer,name='trailerUpd'),
    path('data/trailerDel', deleteTrailer, name='trailerDel'),
    # дукция
    path('data/productionShow', showProduction, name='productionShow'),
    path('data/productionAdd', AddProduction, name='productionAdd'),
    path('data/productionUpd', UpdProduction, name='productionUpd'),
    path('data/productionDel', deleteProduction, name='productionDel'),
    # отвественные лица
    path('data/personShow', showPerson, name='personShow'),
    path('data/personAdd', AddPerson, name='personAdd'),
    path('data/personUpd', UpdPerson, name='personnUpd'),
    path('data/personDel', deletePerson, name='personDel'),


    path('reportAutoAgent/get', reportAutoAgent, name='reportAutoAgent'),
    path('act/generate/get', actGenerate, name='actGenerate'),
    path('act/generateZD/get', actGenerateZD, name='actGenerateZD'),

    path('search/', serchAuto, name='search'),
]
