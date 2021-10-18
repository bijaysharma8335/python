import json
import numpy as np

# def initializemarker(): 
# load json file and initilalize Marker 
f = open("data.json")
 
Marker = json.load(f)

# print(Marker) 


def  DescribeISOPerimeter( Perimetro,  ToolUp, ToolDown, UnitConversion = 1):
    isoStr = "*"

    isoStr += ToolUp + "*X" + (int)(Perimetro[0].X / UnitConversion) + "Y" + (int)(Perimetro[0].Y / UnitConversion) + "*" + ToolDown

    for  p in Perimetro:
        
        isoStr += "*X" + (int)(p.X / UnitConversion) + "Y" + (int)(p.Y / UnitConversion) + "*"
        

    return isoStr

def SaveFile( MarkerName,isoStr):
#     dirpath = MarkerName + DefaultFileExtension

#     file.write(Text,dirpath)
     with open(MarkerName + ".cut" , 'w') as m :
          m.write(isoStr)   


def  BtnIsoExport_Click():
     #  Marker information
    MetricUnit = "G71";  #Millimeters
    MarkerName = "TSHIRTEXAMPLE"

    # ISO Commands
    ToolUp = "M15"
    ToolDown = "M14"

    # ISO Header Description
    IsoText = ""
    IsoText += "H1" + MetricUnit + "D2*" + ToolUp + "*M20*" + MarkerName + "*" + ToolUp + "*D2"

    IndexOfShape = 1
    for s in Marker:
            
        # ISO Shape Description
        IsoText += "*N" + IndexOfShape + "*D2*"
        IsoText += DescribeISOPerimeter(s.Perimeter, ToolUp, ToolDown)
        IndexOfShape += 1
            

    # ISO Closing Description
    IsoText += "*D2*M15*M0*"
    IsoText = IsoText.Replace("**", "*")

    #  // Save the ISO file
    SaveFile(MarkerName, IsoText, ".cut")
    