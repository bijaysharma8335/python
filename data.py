import json
import numpy as np
import hpgl
# import os.path

# def initializemarker(): 
# load json file and initilalize Marker 

# f = open("data.json")
Marker = [
    [1944, 6471],
    [3198, 6445],
    [3947, 6461],
    [4289, 6483],
    [4568, 6516],
    [4812, 6560],
    [5022, 6614],
    [5158, 6418],
    [5286, 6262],
    [5409, 6135],
    [5530, 6033],
    [5650, 5954],
    [5769, 5893],
    [5889, 5850],
    [5974, 5831],
    [6162, 5790],
    [6353, 5764],
    [6569, 5752],
    [6795, 5756],
    [7032, 5778],
    [7281, 5818],
    [7544, 5878],
    [7664, 5911],
    [8184, 4289],
    [8038, 4263],
    [7891, 4220],
    [7750, 4163],
    [7617, 4092],
    [7498, 4011],
    [7394, 3920],
    [7305, 3823],
    [7233, 3721],
    [7177, 3615],
    [7137, 3505],
    [7112, 3391],
    [7105, 3317],
    [7121, 3200],
    [7152, 3088],
    [7200, 2980],
    [7262, 2876],
    [7341, 2776],
    [7437, 2683],
    [7547, 2597],
    [7672, 2520],
    [7809, 2456],
    [7954, 2405],
    [8101, 2370],
    [8194, 2356],
    [7690, 729],
    [7421, 795],
    [7165, 841],
    [6922, 869],
    [6692, 878],
    [6473, 871],
    [6355, 860],
    [6176, 833],
    [6000, 793],
    [5878, 760],
    [5758, 711],
    [5639, 644],
    [5520, 557],
    [5400, 447],
    [5278, 311],
    [5150, 143],
    [5055, 0],
    [4830, 54],
    [4583, 95],
    [4300, 125],
    [3956, 143],
    [3330, 149],
    [3229, 149],
    [1975, 111],
    [683, 70],
    [362, 56],
    [57, 40],
    [26, 985],
    [11, 1942],
    [14, 2911],
    [19, 3281],
    [1, 4256],
    [0, 5218],
    [15, 6167],
    [25, 6522],
    [1944, 6471]
  ]  
# Marker = json.load(f)
x = len(Marker)

print("The length is ", x)
# print(Marker)
# class Shape: 
Perimeter = Marker
Perimetro = Marker

# print(Marker) 
def GetRotationText(Rotatezone):
    
    switcher = {
            0: "DI;",
            1: "DI1,1;",
            2: "DI0,1;",
            3: "DI-1,0;", 
            }
    return switcher.get(Rotatezone , "DI;")

def GetFontDimension(XFont = 12 , YFont = 10 , LF = "\n"):
     
     PtToMillimiter = 0.0352777778
     XDime = (XFont * PtToMillimiter)
     YDime = (YFont * PtToMillimiter)
      
     return "SI" + str(round(XDime, 2)).replace("," , " . ") + "," + str(round(YDime, 2)) + LF

def Drawrect( MarkerLength,  MarkerWidth, PenUp, PenDown, UnitConversion = 1, LF = '\n'):
        
     HpglStr = " "
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


def SaveFile( MarkerName,HpglText ):

     with open(MarkerName + ".hpgl" , 'w') as m :
          m.write(HpglText)


# def DescribeHPGLPerimeter( Marker, PenUp,  PenDown,   LF = '\n'):
        
#      HpglStr = ""
#      HpglStr += "LT0;" + LF; # Line type LT0: continuous line
#      HpglStr += PenUp + (str)(Marker[0].X ) + "," + (str)(Marker[0].Y) + ";" + LF
#      for  p in Marker:
#           HpglStr += PenDown + (str)(p.X ) + "," + (str)(p.Y) + ";" + LF
          
#      HpglStr += PenDown + (str)(Marker[0].X ) + "," + (str)(Marker[0].Y) + ";" + LF
#      HpglStr += PenUp + ";" + LF
#      return HpglStr


def ConvertToHpgl():

     LF = "\n"
     PenUp = "PU"
     PenDown = "PD"
     
     # Marker In  formation
     MarkerName = "TSHIRTEXAMPLE"
     # MarkerLength =   np.max(Marker)
     # MarkerWidth  =   np.max(Marker)
     for d in Marker:
        xc = []
        yc = []
     #    print("d is",d[0])
        xc.append(d[0])
        yc.append(d[1])

     print("xc",max(xc))
     print("yc",max(yc))
        
     # y = max(xc)
     # print("XC",xc)
     #   MarkerLength = np.amax(Marker,axis = 1)
     #   MarkerWidth = np.amax(Marker)
     MarkerLength = xc
     MarkerWidth = yc
     # print(len(MarkerLength))
     HpglText = "IN;"
     HpglText += "SP1;" + LF
     HpglText += DesHeadText(MarkerName, MarkerLength, MarkerWidth) 
     
     HpglText += "LO15;" + LF
     HpglText += PenUp + ";" + LF
     
     # for s in Marker:
            
     #            # HPGL Shape Description
     # HpglText += DescribeHPGLPerimeter(Marker, PenUp, PenDown)
            
     HpglText += Drawrect(MarkerLength, MarkerWidth, PenUp, PenDown)
     print(HpglText)
 

     SaveFile(MarkerName , HpglText )
     # SaveFile()


ConvertToHpgl() 
# def DrawMarker():
#      for s in Marker:
#          return s 
# https://sharecad.org/#179f6607-4ff3-4034-9fae-81fd124fc260  