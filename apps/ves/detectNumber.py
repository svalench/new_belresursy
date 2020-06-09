from datetime import datetime
import json

from shutil import copyfile
from django.http import HttpResponse

from nomer.mainTCP import clientTCP


def detectNumber(request):
    now = datetime.now().time()
    now = str(now)
    path1 ='/static/img_car/'+now+"_cam1"
    path2 = '/static/img_car/' + now + "_cam2"
    path3 = '/static/img_car/' + now + "_cam3"
    copyfile('/home/mvlab/new_bel/new_belresursy/static/camera/cam1.jpg', '/home/mvlab/new_bel/new_belresursy/static/img_car/'+now+"_cam1")
    copyfile('/home/mvlab/new_bel/new_belresursy/static/camera/cam2.jpg', '/home/mvlab/new_bel/new_belresursy/static/img_car/' + now + "_cam2")
    copyfile('/home/mvlab/new_bel/new_belresursy/static/camera/cam3.jpg', '/home/mvlab/new_bel/new_belresursy/static/img_car/' + now + "_cam3")

    number=clientTCP(path_to_image=request.POST['path'],port=6010).decode()
    #number2=clientTCP(path_to_image='/home/mvlab/new_bel/new_belresursy/static/camera/cam2.jpg',port=6020).decode()
    payload = {'success': True,'number':number,'number2':number2,'path1':path1,'path2':path2,'path3':path3}
    return HttpResponse(json.dumps(payload, indent=4, sort_keys=True, default=str), content_type='application/json')

