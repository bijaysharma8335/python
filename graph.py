from reportlab.pdfgen import canvas
def bezier(canvas):
 from reportlab.lib.colors import yellow, green, red, black
 from reportlab.lib.units import inch
 i = inch
 d = i/4
 # define the bezier curve control points
 x1,y1, x2,y2, x3,y3, x4,y4 = d,1.5*i, 1.5*i,d, 3*i,d, 5.5*i-d,3*i-d
 
 canvas.bezier(x1,y1, x2,y2, x3,y3, x4,y4)


c = canvas.Canvas("hello.pdf")
bezier(c)
# c.showPage()
c.save()
