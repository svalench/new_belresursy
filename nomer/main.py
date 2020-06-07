import time
import os
import sys

import cv2
import matplotlib.image as mpimg

# ----------------------------------------------------------------------------------------------------------------------
# change this property
NOMEROFF_NET_DIR = os.path.join(os.path.dirname(os.path.realpath(__file__)), os.getcwd())
MASK_RCNN_DIR = os.path.join(NOMEROFF_NET_DIR, 'model')
MASK_RCNN_LOG_DIR = os.path.join(NOMEROFF_NET_DIR, 'logs')
sys.path.append(NOMEROFF_NET_DIR)
print(MASK_RCNN_DIR, MASK_RCNN_LOG_DIR)
# ----------------------------------------------------------------------------------------------------------------------
# Import license plate recognition tools.
from NomeroffNet import filters, RectDetector, TextDetector, OptionsDetector, Detector, textPostprocessing

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

def detect(img):
    print("START RECOGNIZING")

    # img_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'ex2.jpeg')
    # read image in RGB format
    # p.s. opencv read in BGR format
    # img = mpimg.imread(img_path)
    # DETECT
    NP = nnet.detect([img])
    # Generate image mask.
    cv_img_masks = filters.cv_img_mask(NP)

    # Detect points.
    arrPoints = rectDetector.detect(cv_img_masks)
    print(arrPoints)
    zones = rectDetector.get_cv_zonesBGR(img, arrPoints)

    # find standart
    regionIds, stateIds, countLines = optionsDetector.predict(zones)
    regionNames = optionsDetector.getRegionLabels(regionIds)

    # find text with postprocessing by standart
    textArr = textDetector.predict(zones)
    textArr = textPostprocessing(textArr, regionNames)

    return arrPoints, textArr, zones
    # print(textArr)
    # print(time.time() - startTime)

if __name__ == '__main__':
    print(loadModel())
    while 1:
        t1 = time.time()

        _im = cv2.imread('/home/mvlab/belresusrs/static/camera/cam1.jpg')
        im = cv2.cvtColor(_im, (cv2.COLOR_BGR2RGB))
        imDetect = cv2.resize(im.copy(), (640, 480))
        arrPoints, numberText, zones = detect(imDetect)
        if len(zones)>0:
            h, w, _ = zones[0].shape
            number = cv2.resize(zones[0], (w*2, h*2))
            h, w, _ = number.shape
            _im[:h, :w, :] = number
            cv2.imwrite('/home/mvlab/belresusrs/static/camera/_cam1.jpg', _im)
        else:
            cv2.imwrite('/home/mvlab/belresusrs/static/camera/_cam1.jpg', _im)

        # cv2.imwrite('', _im)
        # cv2.imshow('img1', _im)
        # cv2.waitKey()
        print(time.time() - t1)
