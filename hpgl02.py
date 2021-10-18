import json
import numpy as np
import hpgl
import os.path

# def initializemarker(): 
# load json file and initilalize Marker 
f = open("data.json")
 
Marker = json.load(f)

# print(Marker) 
def DescribeHPGLPerimeter( Perimetro, PenUp = None,  PenDown = None, UnitConversion = 1,LF = "\n"):
     HpglStr = ""   
     HpglStr += "LT0;" + LF; # Line type LT0: continuous line
     HpglStr += PenUp + (int)(Perimetro[0].X / UnitConversion) + "," + (int)(Perimetro[0].Y / UnitConversion) + ";" + LF
     for p in Perimetro:
     
          HpglStr += PenDown + (int)(p.X / UnitConversion) + "," + (int)(p.Y / UnitConversion) + ";" + LF

     HpglStr += PenDown + (int)(Perimetro[0].X / UnitConversion) + "," + (int)(Perimetro[0].Y / UnitConversion) 
     + ";" + LF
     HpglStr += PenUp + ";" + LF
     return HpglStr
        

def Drawingrectangle(MarkerLength, MarkerWidth, PenUp,PenDown,UnitConversion = 1, LF = '\n'):
     HpglStr = ""
     HpglStr += PenUp + 0 + "," + 0 + ";" + LF
     HpglStr += PenDown + (int)(MarkerLength / UnitConversion) + "," + 0 + ";" + LF
     HpglStr += PenDown + (int)(MarkerLength / UnitConversion) + "," + (int)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + 0 + "," + (int)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + 0 + "," + 0 + ";" + LF
     HpglStr += PenUp + ";" + LF
     return HpglStr
        
def GetFontDimension(XFont = 12 , YFont = 10 , LF = "/n"):
     
     PtToMillimiter = 0.0352777778
     XDime = (XFont * PtToMillimiter)
     YDime = (YFont * PtToMillimiter)
      
     return "SI" + str(round(XDime, 2)).replace("," , " . ") + "," + str(round(YDime, 2))

def Drawingrectangle( MarkerLength,  MarkerWidth, PenUp, PenDown, UnitConversion = 1, LF = '\n'):
        
     HpglStr = ""
     HpglStr += PenUp + 0 + "," + 0 + ";" + LF
     HpglStr += PenDown + (int)(MarkerLength / UnitConversion) + "," + 0 + ";" + LF
     HpglStr += PenDown + (int)(MarkerLength / UnitConversion) + "," + (int)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + 0 + "," + (int)(MarkerWidth / UnitConversion) + ";" + LF
     HpglStr += PenDown + 0 + "," + 0 + ";" + LF
     HpglStr += PenUp + ";" + LF
     return HpglStr
        

def DescribeHeaderText( MarkerName = None , MarkerLength = None , MarkerWidth = None , UnitConversion = 1 , LF = "\n" ):
     HpglStr = ""
     description = ""
     description += " Name : " +  MarkerName
     description += " Width : " +  MarkerLength
     description += " Length: " + MarkerWidth
     HpglStr = HpglStr + "SP1" + LF
     HpglStr += GetFontDimension() 

    #  HpglStr += GetRotationText(0)
     PosiX = 0
     PosiY = int(MarkerWidth)

     HpglStr += "DT*,1;" + LF
     HpglStr += "PU" + (int)(PosiX / UnitConversion) + "," + (int)(PosiY / UnitConversion) + ";" + LF
     HpglStr += "LB " + description + "*;" + LF

     return HpglStr

# def SaveFile( MarkerName = None , Text = None , DefaultFileExtension = None):
#      dirpath = MarkerName + DefaultFileExtension

#      file.write(Text,dirpath)

def ConvertToHpgl():
    LF = "\n"
    PenUp = "PU"
    PenDown = "PD"
     
    # Marker Information
    MarkerName = "TSHIRTEXAMPLE"
    MarkerLength = Marker.max(Perimeter.max(p : p.X)) - Marker.min(s : s.Perimeter.Max(p : p.X))
    MarkerWidth  = Marker.max(Perimeter.max(p : p.Y)) - Marker.min(s : s.Perimeter.Max(p : p.Y)) 
     
    HpglText = "IN;"
    HpglText += "SP1;" + LF
     
    HpglText += DescribeHeaderText(MarkerName, MarkerLength, MarkerWidth)
    HpglText += "LO15;" + LF
    HpglText += PenUp + ";" + LF
    for s in Marker:
            
                # // HPGL Shape Description
        HpglText += DescribeHPGLPerimeter(s.Perimeter, PenUp, PenDown)
            
    HpglText += Drawingrectangle(MarkerLength, MarkerWidth, PenUp, PenDown)
    print(HpglText)

    HpglText += Drawingrectangle(MarkerLength, MarkerWidth, PenUp, PenDown)
     
     # SaveFile(MarkerName , HpglText , ".plt")


ConvertToHpgl() 