
from apps.ves.snap7_plc import *

def svetoforFromStreetOnScale(request):
    a=PlcRemoteUse("192.168.0.1")
    a.svetoforFromStreetOnScale()

def svetoforFromScaleOnTerritory(request):
    PlcRemoteUse("192.168.0.1").svetoforFromScaleOnTerritory()

def svetoforFromTerritoryOnScale(request):
    PlcRemoteUse("192.168.0.1").svetoforFromTerritoryOnScale()

def svetoforFromScaleOnStreet(request):
    PlcRemoteUse("192.168.0.1").svetoforFromScaleOnStreet()
