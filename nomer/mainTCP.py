import socket
import time
import os
import sys
import matplotlib.image as mpimg
import multiprocessing as mp
from termcolor import cprint
import cv2
import threading
import multiprocessing as MP
# ----------------------------------------------------------------------------------------------------------------------
# change this property
NOMEROFF_NET_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.getcwd())
MASK_RCNN_DIR = os.path.join(NOMEROFF_NET_DIR, 'model')
MASK_RCNN_LOG_DIR = os.path.join(NOMEROFF_NET_DIR, 'logs')
sys.path.append(NOMEROFF_NET_DIR)
print(MASK_RCNN_DIR, MASK_RCNN_LOG_DIR)
# ----------------------------------------------------------------------------------------------------------------------
# Import license plate recognition tools.
sys.path.insert(0, '/home/mvlab/new_bel/new_belresursy/nomer')
from NomeroffNet import filters, RectDetector, TextDetector, OptionsDetector, Detector, textPostprocessing

def saveIMG(image, path='/home/MV/dataSet'):
    PATH_TO_FOLDER = path
    FOLDER_NAME = time.strftime("%Y-%m-%d")
    _PATH = os.path.join(PATH_TO_FOLDER, FOLDER_NAME)
    # проверка наличия пути, если нет, то создаем папку
    if os.path.exists(_PATH):
        pass
    # print('OK')
    else:
        try:
            os.makedirs(_PATH)
        except OSError:
            print("Creation of the directory %s failed" % _PATH)
        else:
            print("Successfully created the directory %s " % _PATH)
    # формируем имя файла
    FILE_NAME = '{}.jpg'.format(len(os.listdir(_PATH)) + 1)
    # print(FILE_NAME)
    # сохраняем файл в папку
    cv2.imwrite(_PATH + '/' + FILE_NAME, image)

def loadModel():
    global nnet, textDetector, rectDetector, optionsDetector
    try:
        # Initialize npdetector with default configuration file.
        nnet = Detector(MASK_RCNN_DIR, MASK_RCNN_LOG_DIR)
        nnet.loadModel("latest")

        rectDetector = RectDetector()

        optionsDetector = OptionsDetector()
        optionsDetector.load("latest")

        # Initialize text detector.
        textDetector = TextDetector.get_static_module("eu")()
        textDetector.load("latest")

        return True
    except:
        return False

def detect(path_to_img):
    print("START RECOGNIZING")

    startTime = time.time()
    # DETECT
    img = mpimg.imread(path_to_img)
    # сохраняем изображение для дата сета
    # _img = cv2.imread(path_to_img)
    # saveIMG(img)
    NP = nnet.detect([img])
    # Generate image mask.
    cv_img_masks = filters.cv_img_mask(NP)

    # Detect points.
    arrPoints = rectDetector.detect(cv_img_masks)
    zones = rectDetector.get_cv_zonesBGR(img, arrPoints)
    # if bool(zones):
    #     saveIMG(img)
    # find standart
    regionIds, stateIds, countLines = optionsDetector.predict(zones)
    regionNames = optionsDetector.getRegionLabels(regionIds)

    # find text with postprocessing by standart
    textArr = textDetector.predict(zones)
    textArr = textPostprocessing(textArr, regionNames)
    cprint(textArr, 'blue', attrs=['reverse'])
    print(time.time() - startTime)
    # return textArr
    print(parceNumber(textArr[0]))
    return parceNumber(textArr[0])[1]

def serverTCP(port=6000, host='127.0.0.1'):
    ''' Сервер, ожидает входное соединение для получения данных и отсылает ответ после '''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP
    try:
        s.bind((host, port))
        s.listen()
        cprint('wait connect host: %s, port: %s' % (host, port), 'yellow')

        while True:
            conn, addr = s.accept()
            while True:
                # ts = time.time()
                data = conn.recv(512)
                print(data)
                if len(data)>5:
                    number = detect(data.decode())
                    if len(number)>0:
                        # conn.sendall(str.encode(number[0]))
                        conn.sendall(str.encode(number))

                    else:
                        conn.sendall(b'false')
                if not data:
                    break
            time.sleep(2)
    except Exception as e:
        print("ERROR ", e)
        s.close()
    finally:
        cprint('CLOSE CONNECTION', 'red', attrs=['reverse'])
        s.close()
        time.sleep(2)
        serverTCP(port=port, host=host)

def clientTCP(path_to_image, port=6000, host='127.0.0.1'):
    data = str.encode(path_to_image)
    # send data
    s = socket.create_connection((host, port), timeout=60)
    s.sendall(data)
    # recive data
    number = s.recv(512)
    s.close()
    return number

def mainServ(_port, _host='127.0.0.1'):
    try:
        print(loadModel())
        serverTCP(port=_port, host=_host)
    except Exception as e:
        print('ERROR: ', e)
    finally:
        cprint('KILL ALL PROCESS PYTHON3', 'red', attrs=['reverse'])
        os.system('killall -s 9 python3')

def parceNumber(text):
    number = ''
    seria = ''
    region = ''
    typeAuto = 'car' #car, trailer
    t = []
    # проверяем есть ли текст
    if len(text) == 0:
        return [number, seria, region]
    for i in text:
        t.append(i)
    # fix "0" vs "O"
    if not t[0].isdigit() and t[5].isdigit():   # тягач
        if t[1] == '0':
            t[1] = 'O'
        if t[2] == "O":
            t[2] = '0'
        if t[3] == "O":
            t[3] = '0'
        if t[4] == "O":
            t[4] = '0'
        if t[5] == "O":
            t[5] = '0'
    if not t[0].isdigit() and not t[5].isdigit():   # прицеп
        if t[5] == '0':
            t[5] = 'O'
        if t[1] == "O":
            t[1] = '0'
        if t[2] == "O":
            t[2] = '0'
        if t[3] == "O":
            t[3] = '0'
        if t[4] == "O":
            t[4] = '0'

    # если распознан целый номер (7 символов)
    if len(text) == 7:
        # тип авто (прицеп - 1, тягач - 0)
        if not t[0].isdigit() and not t[5].isdigit():
            typeAuto = 'trailer'

        # проверяем регион
        if not t[-1].isdigit() and t[-1] == 'T':
            region = '7'
        else:
            region = t[-1]
    # серия / номер
    for i in t:
        if not i.isdigit():
            if len(seria) < 2:
                seria = seria + i
        else:
            if len(number) < 4:
                number = number + i

    return ([number, seria, region, typeAuto], number+seria+region+typeAuto)

if __name__ == '__main__':
    c1 = MP.Process(target=mainServ, args=[6030, ])
    c2 = MP.Process(target=mainServ, args=[6020, ])
    c1.start()
    c2.start()
    c1.join()
    c2.join()

