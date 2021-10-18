import numpy as np
import pandas as pd
import json
import hpgl

def initializeMarker():
    Marker = []

    print("----------------")


initializeMarker()
# def drawMarker():
#    for s in Marker:
#       return 5


def SaveFile(MarkerName=None, Text=None, DefaultFileExtension=None):
    initializeMarker()


# # drawMarker()
def BtnHpgl_Click():
    LF = "\n"
    PenUp = "PU"
    PenDown = "PD"
    # Marker Information
    MarkerName = "TSHIRTEXAMPLE"
    MarkerLength =
    MarkerWidth =

    HpglText = "IN;"
    HpglText += "SP1;" + LF
    # HpglText += DescribeHeaderText(MarkerName, MarkerLength, MarkerWidth)
    HpglText += "LO15;" + LF
    HpglText += PenUp + ";" + LF

    # for s in Marker:
    #      HpglText += DescribeHPGLPerimeter(s.Perimeter, PenUp, PenDown)

    # HpglText += Drawingrectangle(MarkerLength, MarkerWidth, PenUp, PenDown)
    SaveFile(MarkerName, HpglText, ".plt")


def DescribeHeaderText(MarkerName=None, MarkerLength=None, MarkerWidth=None, UnitConversion=1, LF='\n'):
    HpglStr = ""
    description = ""
    description += " Name : " + MarkerName
    description += " Width : " + MarkerLength
    description += " Length: " + MarkerWidth
    HpglStr = HpglStr + "SP1" + LF
    HpglStr += GetFontDimension()

    HpglStr += GetRotationText(0)
    PosiX = 0
    PosiY = int(MarkerWidth)

    HpglStr += "DT*,1;" + LF
    HpglStr += "PU" + (int)(PosiX / UnitConversion) + "," + \
        (int)(PosiY / UnitConversion) + ";" + LF
    HpglStr += "LB " + description + "*;" + LF

    return HpglStr
    
def Drawingrectangle( MarkerLength,  MarkerWidth, PenUp, PenDown, UnitConversion = 1, LF = '\n'):
        
     HpglStr = ""
     HpglStr += PenUp + 0 + "," + 0 + ";" + LF
     HpglStr += PenDown + (int)(MarkerLength / UnitConversion) + "," + 0 + ";" + LF
     HpglStr += PenDown + (int)(MarkerLength / UnitConversion) + "," + (int)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + 0 + "," + (int)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + 0 + "," + 0 + ";" + LF
     HpglStr += PenUp + ";" + LF
     return HpglStr
        


def GetFontDimension(XFont=12, YFont=10, LF='/n'):
    PtToMillimiter = 0.0352777778
    XDime = (XFont * PtToMillimiter)
    YDime = (YFont * PtToMillimiter)

    return "SI" + str(round(XDime, 2)).replace(",", ".") + "," + str(round(YDime, 2))


def GetRotationText(Rotatezone = None):
    
    switcher = {
            0: "DI;",
            1:"DI1,1;",
            2: "DI0,1;",
            3:"DI-1,0;",
            }
    return switcher.get(Rotatezone , "DI;")
    # return testoRotazione