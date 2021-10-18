from reportlab.lib import colors
from reportlab.graphics.shapes import *
from reportlab.graphics import shapes

d = shapes.Drawing(400, 200)
d.add(Circle(100,90,50, fillColor=colors.blue))
d.add(String(150,100, 'Hello World', fontSize=18, fillColor=colors.red))
d.add(String(180,86, 'Special characters \
 \xc2\xa2\xc2\xa9\xc2\xae\xc2\xa3\xce\xb1\xce\xb2',
fillColor = colors.red))
d.add(Bezier(23,34,34,34,78,89,90,100))
from reportlab.graphics import renderPDF
renderPDF.drawToFile(d, 'example1.pdf', 'My First Drawing')
# def bezier(canvas):
#  from reportlab.lib.colors import yellow, green, red, black
#  from reportlab.lib.units import inch
#  i = inch
#  d = i/4
#  # define the bezier curve control points
#  x1,y1, x2,y2, x3,y3, x4,y4 = d,1.5*i, 1.5*i,d, 3*i,d, 5.5*i-d,3*i-d
#  # draw a figure enclosing the control points
#  canvas.setFillColor(yellow)
#  p = canvas.beginPath()
#  p.moveTo(x1,y1)
#  for (x,y) in [(x2,y2), (x3,y3), (x4,y4)]:
#     p.lineTo(x,y)
#  canvas.drawPath(p, fill=1, stroke=0)
#  # draw the tangent lines
#  canvas.setLineWidth(inch*0.1)
#  canvas.setStrokeColor(green)
#  canvas.line(x1,y1,x2,y2)
#  canvas.setStrokeColor(red)
#  canvas.line(x3,y3,x4,y4)
#  # finally draw the curve
#  canvas.setStrokeColor(black)
#  return canvas.bezier(x1,y1, x2,y2, x3,y3, x4,y4)