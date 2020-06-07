from datetime import datetime

from django.http import HttpResponse
from apps.ves.models import Auto, ActionUser, Agent, Vagon
from apps.ves.docGenerator import redactDocx


def actGenerate(request):
    form = request.POST
    form._mutable = True
    print(form)
    auto = Auto.objects.filter(number=form['numberAuto'])
    print(auto)
    if 'actCurrentDateTime' in form:
        form['actCurrentDateTime'] = None
    if 'actDateCommonComming' in form:
        form['actDateCommonComming'] = None
    if 'actDateOut' in form:
        form['actDateOut'] = None
    auto.update(actNumber=form['actNumberAct'],
                datepriemsovmestny=form['actDateCommonComming'], dateotgruzka=form['actDateOut'])

    date = form['actDateCommonComming'].split("T")
    data =date[0]
    vremia = date[1]
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
    auto.update(actNumber=form['actNumberAct'] ,datepriem = form['actCurrentDateTime'], datepriemsovmestny=form['actDateCommonComming'], dateotgruzka=form['actDateOut'])
    now = datetime.now()
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    response['Content-Disposition'] = 'attachment; filename='+"_act__" + dt_string + '.docx'
    doc = redactDocx(path_to_shablon='/home/mvlab/belresusrs/templates/doc/template1.docx', path_to_save_docx='res001.docx', Data=data_act,response=response)
    return response
