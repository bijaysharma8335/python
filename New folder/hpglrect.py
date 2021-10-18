import json
import numpy as np
# import hpgl
# import os.path
# from Tkinter import *
# def initializemarker(): 
# load json file and initilalize Marker 
# f = open("data.json")
 
# Marker = json.load(f)

# print(Marker) 
def GetRotationText(Rotatezone):
    
    switcher = {
            0: "DI;",
            1:"DI1,1;",
            2: "DI0,1;",
            3:"DI-1,0;",
            }
            
    return switcher.get(Rotatezone , "DI;")

def GetFontDimension(XFont = 12 , YFont = 10 , LF = "\n"):
     
     PtToMillimiter = 0.0352777778
     XDime = (XFont * PtToMillimiter)
     YDime = (YFont * PtToMillimiter)
      
     return "SI" + str(round(XDime, 2)).replace("," , " . ") + "," + str(round(YDime, 2)) + LF

def Drawingrectangle( MarkerLength,  MarkerWidth, PenUp, PenDown, UnitConversion = 1, LF = '\n'):
        
     HpglStr = ""
     HpglStr += PenUp + str(0) + "," + str(0) + ";" + LF
     HpglStr += PenDown + (str)(MarkerLength / UnitConversion) + "," +str(0)  + ";" + LF
     HpglStr += PenDown + (str)(MarkerLength / UnitConversion) + "," + (str)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown +str(0) + "," + (str)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + str(0) + "," + str(0) + ";" + LF
     HpglStr += PenUp + ";" + LF
     return HpglStr
        
    
def DesHeadText( MarkerName , MarkerLength , MarkerWidth, UnitConversion = 1 , LF = "\n" ):
     HpglStr = ""
     description = ""
     description += " Name : " +  (MarkerName)
     description += " Width : " + str (MarkerWidth)
     description += " Length: " + str(MarkerLength)
     HpglStr = HpglStr + "SP1" + LF
     HpglStr += GetFontDimension() 

     HpglStr += GetRotationText(0) 
     PosiX = 0
     PosiY = int(MarkerWidth)

     HpglStr += "DT*,1;" + LF
     HpglStr += "PU" + (str)(PosiX / UnitConversion) + "," + (str)(PosiY / UnitConversion) + ";" + LF
     HpglStr += "LB " + description + "*;" + LF

     return HpglStr

# def SaveFile( MarkerName = None , Text = None , DefaultFileExtension = None):
#      dirpath = MarkerName + DefaultFileExtension

#      file.write(Text,dirpath)
def SaveFile( MarkerName,HpglText ):
#     dirpath = MarkerName + DefaultFileExtension

#     file.write(Text,dirpath)
     with open(MarkerName + ".hpgl" , 'w') as m :
          m.write(HpglText)

def ConvertToHpgl():
     LF = "\n"
     PenUp = "PU"
     PenDown = "PD"
     
     # Marker In  formation
     MarkerName = "RECTANGLE"
     # MarkerLength = Marker.max() - Marker.min()
     # MarkerWidth  = Marker.max() - Marker.min() 
     MarkerLength = 10
     MarkerWidth = 10 
     
     HpglText = "IN;"
     HpglText += "SP1;" + LF
     
     HpglText += DesHeadText(MarkerName, MarkerLength, MarkerWidth)
     HpglText += "LO15;" + LF
     HpglText += PenUp + ";" + LF
     HpglText += Drawingrectangle(MarkerLength, MarkerWidth, PenUp, PenDown)
     print(HpglText)

  
     SaveFile(MarkerName , HpglText )
     # SaveFile(MarkerName , HpglText , ".plt")


ConvertToHpgl() 