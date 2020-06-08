
from apps.ves.snap7_plc import *

def svetoforFromStreetOnScale(request):
    PlcRemoteUse("192.168.0.2").svetoforFromStreetOnScale()

def svetoforFromScaleOnTerritory(request):
    PlcRemoteUse("192.168.0.2").svetoforFromScaleOnTerritory()

def svetoforFromTerritoryOnScale(request):
    PlcRemoteUse("192.168.0.2").svetoforFromTerritoryOnScale()

def svetoforFromScaleOnStreet(request):
    PlcRemoteUse("192.168.0.2").svetoforFromScaleOnStreet()