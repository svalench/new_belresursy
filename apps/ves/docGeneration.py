from datetime import datetime

from django.http import HttpResponse
from apps.ves.models import Auto, ActionUser, Agent, Vagon
from apps.ves.docGenerator import redactDocx
from apps.ves.xlsGenerotor import *


def actGenerate(request):
    form = request.POST
    form._mutable = True
    print(form)
    auto = Auto.objects.filter(number=form['numberAuto'],netto=form['actFactWeight'])
    print(auto)
    if 'actCurrentDateTime' in form:
        form['actCurrentDateTime'] = None
    #if 'actDateCommonComming' in form:
        #form['actDateCommonComming'] = ''
    if 'actDateOut' in form:
        form['actDateOut'] = None
    
    print(form['actDateCommonComming'])
    date = form['actDateCommonComming'].split("T")
    data =date[0]
    vremia = date[1]
    auto.update(actNumber=form['actNumberAct'],
                datepriemsovmestny=data, dateotgruzka=form['actDateOut'])
    data_act = {
        'act_number': form['actNumberAct'], 'date': data, 'time': vremia,
        'position01': form['actLoginUserProf'], 'name01': form['actLoginUserName'],
        'position02': form['actUserProf1'], 'name02': form['actUserName1'],
        'position03': form['actUserProf2'], 'name03': form['actUserName2'],
        'position04': form['actUserProf3'], 'name04': form['actUserName3'],
        'seller_name': form['actContragent'],
        'seller_addres': form['actAddressContragent'],
        'number_date_contract': form['datecontract'],
        'contract_date': form['actDateOut'],
        'type_transport': 'type_transport',
        'number_transport': form['actNameAuto'],
        'type_documents': form['actViewTmc'],
        'number_documents': form['actNumberInvoice'],
        'date_documents': form['actDateInvoice'],
        'date_arrival': form['actDateIn'],
        'weight_consignment': form['actWeightInvoice'],
        'weight_transport_with_cargo': form['actFullWeight'],
        'weight_transport_without_cargo': form['actEmptyWeight'],
        'actual_weight': form['actFactWeight'],
        'weight_deficit': form['actNotWeight'],
        'weediness': form['actPercentDirt'],
        'load_weight': form['actOkWeight']
    }
    auto = Auto.objects.filter(number = form['numberAuto'])
    print(auto)
    if 'actCurrentDateTime' in form:
        form['actCurrentDateTime']=None
    if 'actDateCommonComming' in form:
        form['actDateCommonComming']=None
    if 'actDateOut' in form:
        form['actDateOut']=None
    #auto.update(actNumber=form['actNumberAct'] ,datepriem = form['actCurrentDateTime'], datepriemsovmestny=form['actDateCommonComming'], dateotgruzka=form['actDateOut'])
    now = datetime.now()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    response['Content-Disposition'] = 'attachment; filename='+"_act__" + dt_string + '.docx'
    doc = redactDocx(path_to_shablon='/home/mvlab/new_bel/new_belresursy/templates/doc/template1.docx', path_to_save_docx='res001.docx', Data=data_act,response=response)
    return response


path00 = '/home/mvlab/new_bel/new_belresursy/templates/doc/auto/invoice_horizontal/cvetmet.xlsx'
path01 = '/home/mvlab/new_bel/new_belresursy/templates/doc/auto/invoice_horizontal/chermet.xlsx'
path02 = '/home/mvlab/new_bel/new_belresursy/templates/doc/auto/invoice_horizontal/pet.xlsx'
path_vert = '/home/mvlab/new_bel/new_belresursy/templates/doc/auto/invoice_vertical/gen.xlsx'
def nakladnaia_book(request):
    form = request.POST
    form._mutable = True
    print(form)
    if (form['number_trailer'] == 'null'):
        form['number_trailer'] = ""
    dataInvoice = {
        'unpGruzopoluchatel':form['unp'],
        'date': form['CurrentDate'],  # дата
        'auto': form['number'],  # автомобиль
        'trailer':form['number_trailer'],  # прицеп
        'waybill': form['NumberWayList'],  # путевой лист
        'auto_owner': form['Contragent'],  # владелец автомобильной перевозки (плательщик)
        'driver': form['driver'],  # водитель

        'customer_transportation': '',  # заказчик автомобильной перевозки
        'shipper': '',  # грузоотправитель
        'consignee': form['Contragent'],  # грузополучатель
        'osnovanie_otpuska': '',  # основание отпуска
        'loading_point': '',  # пункт загрузки
        'unloading_point': form['AddressOut'],  # пункт разгрузки

        # ТОВАРНЫЙ РАЗДЕЛ
        'name_tovar': form['NameTmc'],
        'value_name': form['UnitWeight'],
        'value': form['CellPhysicalWeight'],  # количество
        'price': form['CellFirstPrice'],  # цена
        'netto': form['CellSumWithoutNds'],  # стоимость
        'vatSP': form['CellPercentNds'],  # ставка НДС
        'vat': float(form['CellSumNds']),  # сумма НДС
        'brutto': float(form['CellSumWithNds']),  # стоимость с НДС
        'value_place': form['NumberLoadPlace'],  # колличество грузовых мест
        'weight': float(form['CellPhysicalWeight']),  # массв груза

        # ПОГРУЗОЧНО-РАЗГРУЗОЧНЫЕ РАБОТЫ
        'time_arrival': form['last_in'].split(".")[0],  # время прибытия
        'time_depart': form['last_out'].split(".")[0],  # время убытия
    }
    now = datetime.now()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    response['Content-Disposition'] = 'attachment; filename='+"nakladnaya"+form['number']+ "_"+ dt_string + '.xlsx'
    doc = invoiceBelcvetmet(path_to_SH=path00, path_to_save='res001.xlsx', Data=dataInvoice,response=response)
    return response


def nakladnaia_vertical(request):
    form = request.POST
    form._mutable = True
    print(form)
    dataInvoice = {
        'unpGruzopoluchatel': form['unp'],
        'date': form['CurrentDate'],  # дата
        'auto': form['number'],  # автомобиль
        'trailer': form['number_trailer'],  # прицеп
        'waybill': form['NumberWayList'],  # путевой лист
        'auto_owner': form['Contragent'],  # владелец автомобильной перевозки (плательщик)
        'driver': form['driver'],  # водитель

        'customer_transportation': '',  # заказчик автомобильной перевозки
        'shipper': '',  # грузоотправитель
        'consignee': form['Contragent'],  # грузополучатель
        'osnovanie_otpuska': '',  # основание отпуска
        'loading_point': '',  # пункт загрузки
        'unloading_point': form['AddressOut'],  # пункт разгрузки

        # ТОВАРНЫЙ РАЗДЕЛ
        'name_tovar': form['NameTmc'],
        'value_name': form['UnitWeight'],
        'value': form['CellPhysicalWeight'],  # количество
        'price': form['CellFirstPrice'],  # цена
        'netto': form['CellSumWithoutNds'],  # стоимость
        'vatSP': form['CellPercentNds'],  # ставка НДС
        'vat': float(form['CellSumNds']),  # сумма НДС
        'brutto': float(form['CellSumWithNds']),  # стоимость с НДС
        'value_place': form['NumberLoadPlace'],  # колличество грузовых мест
        'weight': float(form['CellPhysicalWeight']),  # массв груза

        # ПОГРУЗОЧНО-РАЗГРУЗОЧНЫЕ РАБОТЫ
        'time_arrival': form['last_in'].split(".")[0],  # время прибытия
        'time_depart': form['last_out'].split(".")[0],  # время убытия
    }
    now = datetime.now()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    response['Content-Disposition'] = 'attachment; filename='+"_act__" + dt_string + '.xlsx'
    doc = invoiceBelcvetmetH(path_to_SH=path_vert, path_to_save='res001.xlsx', Data=dataInvoice,response=response)
    return response
